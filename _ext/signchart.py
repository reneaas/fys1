"""signchart directive: build a sign chart using the signchart module.

Usage (MyST):

:::{signchart}
---
function: x**2 - 4, f(x)
factors: true
width: 100%
---
Optional caption text
:::
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import uuid
from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


# ------------------------------------
# Utilities
# ------------------------------------


def _hash_key(*parts) -> str:
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


def _safe_literal(val: str):
    import ast

    try:
        return ast.literal_eval(val)
    except Exception:
        return None


def _parse_bool(val, default: bool | None = None) -> bool | None:
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    if s == "":
        return True
    if s in {"true", "yes", "on", "1"}:
        return True
    if s in {"false", "no", "off", "0"}:
        return False
    return default


def _strip_root_svg_size(svg_text: str) -> str:
    def repl(m):
        tag = m.group(0)
        tag = re.sub(r'\swidth="[^"]+"', "", tag)
        tag = re.sub(r'\sheight="[^"]+"', "", tag)
        return tag

    return re.sub(r"<svg\b[^>]*>", repl, svg_text, count=1)


def _rewrite_ids(txt: str, prefix: str) -> str:
    ids = re.findall(r'\bid="([^"]+)"', txt)
    if not ids:
        return txt
    skip_prefixes = (
        "DejaVu",
        "CM",
        "STIX",
        "Nimbus",
        "Bitstream",
        "Arial",
        "Times",
        "Helvetica",
    )
    mapping = {}
    for i in ids:
        if i.startswith(skip_prefixes):
            continue
        mapping[i] = f"{prefix}{i}"
    if not mapping:
        return txt

    def repl_id(m: re.Match) -> str:
        old = m.group(1)
        new = mapping.get(old, old)
        return f'id="{new}"'

    txt = re.sub(r'\bid="([^"]+)"', repl_id, txt)

    def repl_url(m: re.Match) -> str:
        old = m.group(1).strip()
        new = mapping.get(old, old)
        return f"url(#{new})"

    txt = re.sub(r"url\(#\s*([^\)\s]+)\s*\)", repl_url, txt)

    def repl_href(m: re.Match) -> str:
        attr = m.group(1)
        quote = m.group(2)
        old = m.group(3).strip()
        new = mapping.get(old, old)
        return f"{attr}={quote}#{new}{quote}"

    txt = re.sub(r'(xlink:href|href)\s*=\s*(["\"])#\s*([^"\"]+)\s*\2', repl_href, txt)
    return txt


class SignChartDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        # presentation / misc
        "width": directives.length_or_percentage_or_unitless,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,
        "nocache": directives.flag,
        "debug": directives.flag,
        "alt": directives.unchanged,
        # specific options
        "function": directives.unchanged_required,  # e.g. "x**2 - 4, f(x)"
        "factors": directives.unchanged,  # default True
    }

    def _parse_kv_block(self) -> Tuple[Dict[str, Any], int]:
        lines = list(self.content)
        scalars: Dict[str, Any] = {}
        idx = 0
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                if not line.strip():
                    idx += 1
                    continue
                m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
                if m:
                    scalars[m.group(1)] = m.group(2)
                idx += 1
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return scalars, idx

        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
            if m:
                scalars[m.group(1)] = m.group(2)
                caption_start = i + 1
            else:
                break
        return scalars, caption_start

    def run(self):  # noqa: C901
        env = self.state.document.settings.env
        app = env.app
        try:
            import signchart  # type: ignore
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(text=f"Kunne ikke importere signchart: {e}")
            return [err]

        scalars, caption_idx = self._parse_kv_block()
        merged: Dict[str, Any] = {**scalars, **self.options}

        func_raw = merged.get("function")
        if not func_raw:
            return [
                self.state_machine.reporter.error(
                    "Directive 'signchart' krever 'function:'", line=self.lineno
                )
            ]

        # Parse function as either (expr, label) literal or "expr, label"
        f_expr = None
        f_name = None
        lit = _safe_literal(str(func_raw))
        if isinstance(lit, (list, tuple)) and len(lit) >= 1:
            f_expr = str(lit[0]).strip()
            if len(lit) > 1:
                f_name = str(lit[1]).strip() or None
        else:
            s = str(func_raw)
            if "," in s:
                expr, label = s.split(",", 1)
                f_expr = expr.strip()
                label = label.strip()
                f_name = label or None
            else:
                f_expr = s.strip()
                f_name = None

        include_factors = _parse_bool(merged.get("factors"), default=True)
        explicit_name = merged.get("name")
        debug_mode = "debug" in merged

        # Hash includes function, name, and factors
        content_hash = _hash_key(f_expr, f_name or "", int(bool(include_factors)))
        base_name = explicit_name or f"signchart_{content_hash}"

        rel_dir = os.path.join("_static", "signchart")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        if regenerate:
            try:
                # Render using signchart and save as SVG
                signchart.plot(
                    f=f_expr,
                    fn_name=f_name or None,
                    include_factors=bool(include_factors),
                )
                signchart.savefig(dirname=abs_dir, fname=svg_name)
            except Exception as e:
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av fortegnsskjema: {e}",
                        line=self.lineno,
                    )
                ]

        if not os.path.exists(abs_svg):
            return [
                self.state_machine.reporter.error(
                    "signchart: SVG mangler.", line=self.lineno
                )
            ]

        env.note_dependency(abs_svg)
        # copy into build _static
        try:
            out_static = os.path.join(app.outdir, "_static", "signchart")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"signchart inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

        if not debug_mode and "viewBox" in raw_svg:
            raw_svg = _strip_root_svg_size(raw_svg)

        if not debug_mode:
            raw_svg = _rewrite_ids(
                raw_svg, f"sgc_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = "Fortegnsskjema"
        alt = merged.get("alt", alt_default)

        width_opt = merged.get("width")
        percent = isinstance(width_opt, str) and width_opt.strip().endswith("%")

        def _augment(m):
            tag = m.group(0)
            if "class=" not in tag:
                tag = tag[:-1] + ' class="graph-inline-svg"' + ">"
            else:
                tag = tag.replace('class="', 'class="graph-inline-svg ')
            if alt and "aria-label=" not in tag:
                tag = tag[:-1] + f' role="img" aria-label="{alt}"' + ">"
            if width_opt:
                if percent:
                    wval = width_opt.strip()
                else:
                    wval = width_opt.strip()
                    if wval.isdigit():
                        wval += "px"
                style_frag = f"width:{wval}; height:auto; display:block; margin:0 auto;"
                if "style=" in tag:
                    tag = re.sub(
                        r'style="([^"]*)"',
                        lambda mm: f'style="{mm.group(1)}; {style_frag}"',
                        tag,
                        count=1,
                    )
                else:
                    tag = tag[:-1] + f' style="{style_frag}"' + ">"
            return tag

        raw_svg = re.sub(r"<svg\b[^>]*>", _augment, raw_svg, count=1)
        if alt and "<title" not in raw_svg:
            raw_svg = re.sub(
                r"(<svg\b[^>]*>)",
                r"\1<title>" + re.escape(alt) + r"</title>",
                raw_svg,
                count=1,
            )

        figure = nodes.figure()
        figure.setdefault("classes", []).extend(
            ["adaptive-figure", "signchart-figure", "no-click"]
        )
        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            ["graph-image", "no-click", "no-scaled-link"]
        )
        figure += raw_node

        extra_classes = merged.get("class")
        if extra_classes:
            figure["classes"].extend(extra_classes)
        figure["align"] = merged.get("align", "center")

        caption_lines = list(self.content)[caption_idx:]
        while caption_lines and not caption_lines[0].strip():
            caption_lines.pop(0)
        if caption_lines:
            caption = nodes.caption()
            caption += nodes.Text("\n".join(caption_lines))
            figure += caption

        if explicit_name := merged.get("name"):
            self.add_name(figure)
        return [figure]


def setup(app):  # pragma: no cover
    app.add_directive("signchart", SignChartDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
