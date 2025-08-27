"""multi-plot2 directive: arrange multiple plot directives in a grid.

Usage (MyST):

::::{multi-plot2}
---
rows: 2
cols: 2
width: 100%
# gap: 12px
# align: center  # left|center|right
---
:::{plot}
function: x**2 - 3*x + 2, A
:::

:::{plot}
function: 2*x + 1, B
:::

:::{plot}
function: cos(x), C
:::

:::{plot}
function: 2 / (x + 1), D
domains: (-10, 10) \ {-1}
:::
::::

This directive simply parses its content (which should contain one or more
plot directives) and wraps the resulting figures into a responsive CSS grid.
It doesn't regenerate or modify the inner plots; it just arranges them.
"""

from __future__ import annotations

import os
import re
import uuid
import hashlib
import shutil
from typing import Dict, Tuple, List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class MultiPlot2Directive(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        "rows": directives.unchanged,  # integer
        "cols": directives.unchanged,  # integer
        "width": directives.length_or_percentage_or_unitless,  # e.g. 100%, 800, 800px
        "gap": directives.unchanged,  # e.g. 8px
        "scale": directives.unchanged,  # optional scale factor for each tile
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,
        "alt": directives.unchanged,
    }

    def _gather_kv_from_content(self) -> Tuple[Dict[str, str], int]:
        kv: Dict[str, str] = {}
        lines = list(self.content)
        idx = 0
        # YAML front matter style
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
                if m:
                    kv[m.group(1)] = m.group(2)
                idx += 1
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return kv, idx
        # flat key: value lines until first non-matching or blank separation
        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
            if m:
                kv[m.group(1)] = m.group(2)
                caption_start = i + 1
            else:
                break
        return kv, caption_start

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        # Parse simple options
        def _parse_int(val, default):
            try:
                return int(float(val))
            except Exception:
                return default

        def _parse_float(val, default):
            try:
                return float(val)
            except Exception:
                return default

        kv, inner_idx = self._gather_kv_from_content()
        rows = _parse_int(self.options.get("rows", kv.get("rows", 1)), 1)
        cols = _parse_int(self.options.get("cols", kv.get("cols", 2)), 2)
        width_opt = self.options.get("width", kv.get("width"))
        gap_opt = self.options.get("gap", kv.get("gap", "0"))
        scale_opt = _parse_float(self.options.get("scale", kv.get("scale", 1.0)), 1.0)
        align_opt = self.options.get("align", kv.get("align", "center"))
        alt = self.options.get("alt", kv.get("alt", "Sammensatt figur"))
        extra_classes = self.options.get("class")
        explicit_name = self.options.get("name")
        holder = nodes.Element()
        remaining = self.content[inner_idx:]

        # Convert inner MyST ':::{plot} ... :::' blocks into reST '.. plot::' blocks
        # so nested_parse (RST parser) can execute them.
        def _convert_myst_plot_to_rst(lines: List[str]) -> List[str]:
            out: List[str] = []
            in_plot = False
            for ln in lines:
                s = ln.rstrip("\n")
                if not in_plot and re.match(r"^\s*:::\{\s*plot\s*\}\s*$", s):
                    out.append(".. plot::")
                    in_plot = True
                    continue
                if in_plot:
                    if re.match(r"^\s*:::\s*$", s):
                        in_plot = False
                        out.append("")  # blank line to end directive block
                        continue
                    out.append("   " + s)
                    continue
                out.append(s)
            return out

        parse_lines = _convert_myst_plot_to_rst(list(remaining))
        if parse_lines:
            self.state.nested_parse(
                parse_lines, self.content_offset + inner_idx, holder
            )

        def _collect_raw_svgs(node: nodes.Node, acc: List[str]):
            if isinstance(node, nodes.raw) and getattr(node, "format", "") == "html":
                txt = node.astext()
                if "<svg" in txt:
                    acc.append(txt)
            for ch in getattr(node, "children", []) or []:
                _collect_raw_svgs(ch, acc)

        raw_svgs: List[str] = []
        for ch in holder.children:
            _collect_raw_svgs(ch, raw_svgs)
        holder.children[:] = []
        if not raw_svgs:
            err = nodes.error()
            err += nodes.paragraph(
                text=(
                    "multi-plot2: Fant ingen SVG-er fra underliggende plot. "
                    "Sjekk at blokkene inne i multi-plot2 inneholder {plot}-direktiver."
                )
            )
            return [err]
        try:
            from svgutils.compose import Figure, SVG  # type: ignore
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(
                text=(
                    f"multi-plot2: svgutils mangler eller kunne ikke lastes ({e}). "
                    "Legg til 'svgutils' i requirements.txt eller installer pakken."
                )
            )
            return [err]

        def _extract_dims(svg_txt: str) -> Tuple[float, float]:
            m = re.search(r'viewBox\s*=\s*"([^"]+)"', svg_txt)
            if m:
                parts = [p for p in m.group(1).strip().split() if p]
                if len(parts) == 4:
                    try:
                        return float(parts[2]) * scale_opt, float(parts[3]) * scale_opt
                    except Exception:
                        pass
            mw = re.search(r'\bwidth\s*=\s*"([0-9.]+)\s*(?:px)?"', svg_txt)
            mh = re.search(r'\bheight\s*=\s*"([0-9.]+)\s*(?:px)?"', svg_txt)
            try:
                wv = float(mw.group(1)) if mw else 640.0
                hv = float(mh.group(1)) if mh else 480.0
            except Exception:
                wv, hv = 640.0, 480.0
            return wv * scale_opt, hv * scale_opt

        base_hash = hashlib.sha1("".join(raw_svgs).encode("utf-8")).hexdigest()[:10]
        content_hash = hashlib.sha1(
            f"{rows}|{cols}|{gap_opt}|{scale_opt}|{base_hash}".encode("utf-8")
        ).hexdigest()[:12]
        base_name = explicit_name or f"multi_plot2_{content_hash}"
        rel_dir = os.path.join("_static", "multi_plot2", base_name)
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        paths: List[str] = []
        dims: List[Tuple[float, float]] = []
        for i, svg_txt in enumerate(raw_svgs):
            p = os.path.join(abs_dir, f"tile_{i+1}.svg")
            with open(p, "w", encoding="utf-8") as f:
                f.write(svg_txt)
            paths.append(p)
            dims.append(_extract_dims(svg_txt))
        n = len(paths)
        if rows < 1 and cols < 1:
            import math

            rows = max(1, int(math.floor(math.sqrt(n))))
            cols = max(1, int(math.ceil(n / rows)))
        elif rows < 1:
            import math

            rows = max(1, int(math.ceil(n / max(1, cols))))
        elif cols < 1:
            import math

            cols = max(1, int(math.ceil(n / max(1, rows))))
        import math as _math

        if rows * cols < n:
            rows = int(_math.ceil(n / max(1, cols)))

        def _parse_gap_px(g: str) -> float:
            if not isinstance(g, str):
                return 0.0
            s = g.strip().lower()
            try:
                if s.endswith("px"):
                    return float(s[:-2])
                return float(s)
            except Exception:
                return 0.0

        gap_px = _parse_gap_px(str(gap_opt))
        cell_w = max((w for (w, h) in dims), default=640.0)
        cell_h = max((h for (w, h) in dims), default=480.0)
        total_w = cols * cell_w + max(0, cols - 1) * gap_px
        total_h = rows * cell_h + max(0, rows - 1) * gap_px
        elements = []
        for i, p in enumerate(paths):
            r = i // cols
            c = i % cols
            w_i, h_i = dims[i]
            x0 = c * (cell_w + gap_px) + max(0.0, (cell_w - w_i) / 2.0)
            y0 = r * (cell_h + gap_px) + max(0.0, (cell_h - h_i) / 2.0)
            el = SVG(p).move(x0, y0)
            if scale_opt and scale_opt != 1.0:
                el = el.scale(scale_opt)
            elements.append(el)
        merged_svg_path = os.path.join(abs_dir, f"{base_name}.svg")
        try:
            fig = Figure(total_w, total_h, *elements)
            fig.save(merged_svg_path)
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(text=f"multi-plot2: Feil under sammensetting: {e}")
            return [err]
        try:
            out_static = os.path.join(app.outdir, "_static", "multi_plot2", base_name)
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(merged_svg_path, os.path.join(out_static, f"{base_name}.svg"))
        except Exception:
            pass
        try:
            raw_svg = open(merged_svg_path, "r", encoding="utf-8").read()
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(text=f"multi-plot2: kunne ikke lese SVG: {e}")
            return [err]

        def _strip_root_svg_size(txt: str) -> str:
            def repl(m):
                tag = m.group(0)
                tag = re.sub(r'\swidth="[^"]+"', "", tag)
                tag = re.sub(r'\sheight="[^"]+"', "", tag)
                return tag

            return re.sub(r"<svg\b[^>]*>", repl, txt, count=1)

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

            def repl_id(m):
                old = m.group(1)
                new = mapping.get(old, old)
                return f'id="{new}"'

            txt = re.sub(r'\bid="([^"]+)"', repl_id, txt)

            def repl_url(m):
                old = m.group(1).strip()
                new = mapping.get(old, old)
                return f"url(#{new})"

            txt = re.sub(r"url\(#\s*([^\)\s]+)\s*\)", repl_url, txt)

            def repl_href(m):
                attr = m.group(1)
                quote = m.group(2)
                old = m.group(3).strip()
                new = mapping.get(old, old)
                return f"{attr}={quote}#{new}{quote}"

            txt = re.sub(
                r'(xlink:href|href)\s*=\s*(["\"])#\s*([^"\"]+)\s*\2', repl_href, txt
            )
            return txt

        if "viewBox" in raw_svg:
            raw_svg = _strip_root_svg_size(raw_svg)
        raw_svg = _rewrite_ids(raw_svg, f"mp2_{uuid.uuid4().hex[:6]}_")
        percent = isinstance(width_opt, str) and str(width_opt).strip().endswith("%")

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
                    wval = str(width_opt).strip()
                else:
                    wval = str(width_opt).strip()
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
            ["adaptive-figure", "multi-plot2-figure", "no-click"]
        )
        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            ["graph-image", "no-click", "no-scaled-link"]
        )
        figure += raw_node
        if extra_classes:
            figure.setdefault("classes", []).extend(extra_classes)
        figure["align"] = align_opt
        if explicit_name:
            self.add_name(figure)
        return [figure]


def setup(app):  # pragma: no cover
    app.add_directive("multi-plot2", MultiPlot2Directive)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
