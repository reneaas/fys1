"""plot directive: build a flexible plot using plotmath primitives.

Usage (MyST):

:::{plot}
---
function: x**2 - 2*x + 3
function: -2*x + 3
point: (2, 3)
annotate: [(1, 2), (2, 3), "Label"]
xmin: -6
xmax: 6
ymin: -10
ymax: 10
ticks: true
grid: off
fontsize: 24
width: 100%
---
Optional caption text
:::
"""

from __future__ import annotations

import ast
import hashlib
import os
import re
import shutil
import uuid
from typing import Any, Callable, Dict, List, Tuple

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


def _compile_function(expr: str) -> Callable:
    import sympy, numpy as np

    expr = expr.strip()
    x = sympy.symbols("x")
    try:
        sym = sympy.sympify(expr)
    except Exception as e:
        raise ValueError(f"Ugyldig funksjonsuttrykk '{expr}': {e}")
    fn_np = sympy.lambdify(x, sym, modules=["numpy"])

    def f(arr):
        return fn_np(np.asarray(arr, dtype=float))

    _ = f([0.0, 1.0])
    return f


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


def _safe_literal(val: str):
    try:
        return ast.literal_eval(val)
    except Exception:
        return None


def _split_list(val: str) -> List[str]:
    s = str(val or "").strip()
    if not s:
        return []
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    s = s.replace(";", ",")
    return [p.strip() for p in s.split(",") if p.strip()]


def _parse_text_positioning(pos: str) -> Tuple[str, str]:
    """Map positioning string to (va, ha). Default is (top, left).

    Accepted values (case-insensitive, hyphen or underscore allowed):
      - top-left, top-right, bottom-left, bottom-right,
      - top-center, bottom-center, center-left, center-right
    """
    if not isinstance(pos, str):
        return ("top", "left")
    key = pos.strip().lower().replace("_", "-")

    # Map onto the opposites to make intuitive sense.
    # Matplotlib expects the position to refer to where the object is relative to the text.
    # Thus "left" means the object is to the "left" of the text.
    # Here "left" will mean "move the text to the left of the object"
    mapping = {
        "top-left": ("bottom", "right"),
        "top-right": ("bottom", "left"),
        "bottom-left": ("top", "right"),
        "bottom-right": ("top", "left"),
        "top-center": ("bottom", "center"),
        "bottom-center": ("top", "center"),
        "center-left": ("center", "right"),
        "center-right": ("center", "left"),
        # Longer distance from point
        "longtop-left": ("longbottom", "left"),
        "longtop-longleft": ("longbottom", "longright"),
        "longbottom-right": ("longtop", "right"),
        "longbottom-left": ("longtop", "left"),
        "longtop-center": ("longbottom", "center"),
        "longbottom-center": ("longtop", "center"),
        "longtop-longright": ("longbottom", "longleft"),
        "longbottom-longright": ("longtop", "longleft"),
        "longtop-longleft": ("longbottom", "longright"),
        "longbottom-longleft": ("longtop", "longright"),
        "top-longleft": ("bottom", "longright"),
        "top-longright": ("bottom", "longleft"),
        "bottom-longleft": ("top", "longright"),
        "bottom-longright": ("top", "longleft"),
        "center-longleft": ("center", "longright"),
        "center-longright": ("center", "longleft"),
        "center-center": ("center", "center"),
    }
    return mapping.get(key, ("top", "left"))


class PlotDirective(SphinxDirective):
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
        # axes options (optional in YAML too)
        "xmin": directives.unchanged,
        "xmax": directives.unchanged,
        "ymin": directives.unchanged,
        "ymax": directives.unchanged,
        "xstep": directives.unchanged,
        "ystep": directives.unchanged,
        "fontsize": directives.unchanged,
        "ticks": directives.unchanged,
        "grid": directives.unchanged,
        "lw": directives.unchanged,
        "alpha": directives.unchanged,
        # axis labels
        "xlabel": directives.unchanged,
        "ylabel": directives.unchanged,
    }

    def _parse_kv_block(self) -> Tuple[Dict[str, Any], Dict[str, List[str]], int]:
        """Parse front matter supporting repeated keys for function/point/annotate.

        Returns: (scalars, lists, caption_idx)
        """
        lines = list(self.content)
        scalars: Dict[str, Any] = {}
        lists: Dict[str, List[str]] = {
            "function": [],
            "point": [],
            "annotate": [],
            "text": [],
            "vline": [],
            "hline": [],
            "line": [],
            "polygon": [],
            "axis": [],
            "fill-polygon": [],
            "bar": [],
        }
        # YAML-like fenced front matter
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                if not line.strip():
                    idx += 1
                    continue
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
                if m:
                    key, value = m.group(1), m.group(2)
                    if key in lists:
                        lists[key].append(value)
                    else:
                        scalars[key] = value
                idx += 1
            # Skip closing fence if present
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            # Skip trailing blanks before caption
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return scalars, lists, idx

        # Fallback: non-fenced lines until first non "key: value" or a blank separator
        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
            if m:
                key, value = m.group(1), m.group(2)
                if key in lists:
                    lists[key].append(value)
                else:
                    scalars[key] = value
                caption_start = i + 1
            else:
                break
        return scalars, lists, caption_start

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        try:
            import plotmath  # type: ignore
            import numpy as np  # used for x sampling when plotting functions
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(text=f"Kunne ikke importere plotmath: {e}")
            return [err]

        scalars, lists, caption_idx = self._parse_kv_block()
        merged: Dict[str, Any] = {**scalars, **self.options}

        # debug print removed

        def _f(name, default):
            v = merged.get(name)
            if v in (None, ""):
                return default
            try:
                return float(v)
            except Exception:
                return default

        xmin = _f("xmin", -6)
        xmax = _f("xmax", 6)
        ymin = _f("ymin", -6)
        ymax = _f("ymax", 6)
        xstep = _f("xstep", 1)
        ystep = _f("ystep", 1)
        fontsize = _f("fontsize", 20)
        lw = _f("lw", 2.5)
        alpha_raw = merged.get("alpha")
        try:
            alpha = float(alpha_raw) if alpha_raw not in (None, "") else None
        except Exception:
            alpha = None

        ticks_flag = _parse_bool(merged.get("ticks"), default=None)
        grid_flag = _parse_bool(merged.get("grid"), default=None)
        if ticks_flag is None and grid_flag is None:
            ticks_flag = True
            grid_flag = True
        else:
            ticks_flag = bool(ticks_flag)
            grid_flag = bool(grid_flag)

        # Compile functions (may be zero or many) and parse optional labels, optional domain (xmin,xmax), and optional exclusions
        raw_fn_items = lists.get("function", [])
        fn_exprs: List[str] = []
        fn_labels_list: List[str] = []
        fn_domains_list: List[Tuple[float, float] | None] = []
        fn_exclusions_list: List[List[float]] = []
        functions: List[Callable] = []

        def _parse_function_item(
            s: str,
        ) -> Tuple[str, str | None, Tuple[float, float] | None, List[float]]:
            s = str(s).strip()
            # Try literal list/tuple like ("expr", "label") or ("expr", (xmin,xmax)) or ("expr", "label", (xmin,xmax)) in any order
            lit = _safe_literal(s)
            if isinstance(lit, (list, tuple)) and len(lit) >= 1:
                expr = str(lit[0]).strip()
                label: str | None = None
                domain: Tuple[float, float] | None = None
                excludes: List[float] = []
                for item in list(lit[1:]):
                    # Detect domain tuple/list of two numbers
                    if (
                        domain is None
                        and isinstance(item, (list, tuple))
                        and len(item) == 2
                    ):
                        try:
                            d0 = float(item[0])
                            d1 = float(item[1])
                            domain = (d0, d1)
                            continue
                        except Exception:
                            pass
                    # Detect exclusions as a collection of numbers (not a 2-tuple domain)
                    if isinstance(item, (set, list, tuple)) and not (
                        isinstance(item, (list, tuple)) and len(item) == 2
                    ):
                        for v in item:
                            try:
                                excludes.append(float(v))
                            except Exception:
                                pass
                    # Else treat as label if string-like
                    if label is None and isinstance(item, str):
                        lab = item.strip()
                        label = lab if lab else None
                return expr, label, domain, excludes
            # Fallback: look for a domain pattern (a,b), remove it, then split label
            domain: Tuple[float, float] | None = None
            excludes: List[float] = []
            num_re = r"[+-]?\d+(?:\.\d+)?"
            # Domain with optional set-difference exclusions: (a,b) \ {x1, x2}
            dom_ex_pat = re.compile(
                rf"\(\s*({num_re})\s*,\s*({num_re})\s*\)\s*(?:\\\s*\{{\s*([^}}]*)\s*\}})?"
            )
            m = dom_ex_pat.search(s)
            if m:
                try:
                    d0 = float(m.group(1))
                    d1 = float(m.group(2))
                    domain = (d0, d1)
                except Exception:
                    domain = None
                # Parse exclusions if provided
                excl_str = m.group(3) if m.lastindex and m.lastindex >= 3 else None
                if excl_str:
                    for tok in [t.strip() for t in excl_str.split(",") if t.strip()]:
                        try:
                            excludes.append(float(tok))
                        except Exception:
                            pass
                # Remove the matched domain+exclusions substring
                a, b = m.span()
                s_wo_dom = (s[:a] + s[b:]).strip()
            else:
                s_wo_dom = s
            # Tokenize on commas to robustly drop empty segments created by domain removal
            parts = [p.strip() for p in s_wo_dom.split(",") if p.strip()]
            if parts:
                expr = parts[0]
                label = parts[1] if len(parts) > 1 else None
                return expr, label, domain, excludes
            # Only expression provided (or empty after cleanup)
            return s_wo_dom.strip(), None, domain, excludes

        for item in raw_fn_items:
            expr, label, domain, excludes = _parse_function_item(item)
            try:
                functions.append(_compile_function(expr))
                fn_exprs.append(expr)
                fn_labels_list.append(label or "")
                fn_domains_list.append(domain)
                fn_exclusions_list.append(sorted(excludes))
            except Exception as ex:
                return [
                    self.state_machine.reporter.error(
                        f"Ugyldig funksjon '{expr}': {ex}", line=self.lineno
                    )
                ]

        # Points
        point_vals: List[Tuple[float, float]] = []
        for p in lists.get("point", []):
            lit = _safe_literal(p)
            if isinstance(lit, (list, tuple)) and len(lit) == 2:
                try:
                    x0 = float(lit[0])
                    y0 = float(lit[1])
                    point_vals.append((x0, y0))
                except Exception:
                    pass

        # Annotations: [(xytext), (xy), "text", arc] OR without outer brackets:
        # (xytext), (xy), "text"[, arc]
        ann_vals: List[Tuple[Tuple[float, float], Tuple[float, float], str, float]] = []
        for a in lists.get("annotate", []):
            lit = _safe_literal(a)
            # If user omitted surrounding brackets, try wrapping in [] for parsing
            if not (isinstance(lit, (list, tuple)) and len(lit) >= 3):
                lit_wrapped = _safe_literal(f"[{a}]")
                if isinstance(lit_wrapped, list) and len(lit_wrapped) >= 3:
                    lit = lit_wrapped
            if isinstance(lit, (list, tuple)) and len(lit) >= 3:
                xytext, xy, text = lit[0], lit[1], lit[2]
                arc = float(lit[3]) if len(lit) > 3 else 0.3
                try:
                    xytext = (float(xytext[0]), float(xytext[1]))
                    xy = (float(xy[0]), float(xy[1]))
                    text = str(text)
                    ann_vals.append((xytext, xy, text, arc))
                except Exception:
                    pass

        # Text: x, y, text, optional positioning, optional bbox flag
        # Accepted forms:
        #  - [x, y, text]
        #  - [x, y, text, pos]
        #  - [x, y, text, bbox]  # where bbox can be 'bbox' or a boolean (true/false)
        #  - [x, y, text, pos, bbox]
        # CSV fallback supports the same arities; for 4 tokens, the 4th can be pos or bbox
        text_vals: List[Tuple[float, float, str, str, bool]] = []
        for t in lists.get("text", []):
            lit = _safe_literal(t)
            if isinstance(lit, (list, tuple)) and (3 <= len(lit) <= 5):
                try:
                    x = float(lit[0])
                    y = float(lit[1])
                    text = str(lit[2])
                    pos = "top-left"
                    bbox_flag = False
                    if len(lit) == 4:
                        token = lit[3]
                        # If token is an explicit bbox flag
                        if isinstance(token, str) and token.strip().lower() == "bbox":
                            bbox_flag = True
                        else:
                            b = _parse_bool(token, default=None)
                            if isinstance(b, bool):
                                bbox_flag = bool(b)
                            else:
                                pos = str(token)
                    elif len(lit) == 5:
                        pos = str(lit[3])
                        token = lit[4]
                        if isinstance(token, str) and token.strip().lower() == "bbox":
                            bbox_flag = True
                        else:
                            b = _parse_bool(token, default=None)
                            if isinstance(b, bool):
                                bbox_flag = bool(b)
                    text_vals.append((x, y, text, pos, bbox_flag))
                    continue
                except Exception:
                    pass
            # Fallback: allow unquoted tokens like top-left using a CSV-style parse
            try:
                import csv

                s = str(t).strip()
                # strip surrounding brackets/parentheses if present
                if (s.startswith("[") and s.endswith("]")) or (
                    s.startswith("(") and s.endswith(")")
                ):
                    s = s[1:-1]
                # parse as a single CSV row
                row = next(csv.reader([s], skipinitialspace=True))
                if len(row) in (3, 4, 5):
                    x = float(row[0].strip())
                    y = float(row[1].strip())
                    text = row[2].strip()
                    pos_keys = {
                        "top-left",
                        "top-right",
                        "bottom-left",
                        "bottom-right",
                        "top-center",
                        "bottom-center",
                        "center-left",
                        "center-right",
                    }
                    pos = "top-left"
                    bbox_flag = False
                    if len(row) == 4:
                        tok = row[3].strip()
                        if tok.lower() in pos_keys:
                            pos = tok
                        else:
                            if tok.strip().lower() == "bbox":
                                bbox_flag = True
                            else:
                                b = _parse_bool(tok, default=None)
                                if isinstance(b, bool):
                                    bbox_flag = bool(b)
                                else:
                                    # treat as position if not a boolean
                                    pos = tok
                    elif len(row) == 5:
                        pos = row[3].strip()
                        tok = row[4].strip()
                        if tok.strip().lower() == "bbox":
                            bbox_flag = True
                        else:
                            b = _parse_bool(tok, default=None)
                            if isinstance(b, bool):
                                bbox_flag = bool(b)
                    text_vals.append((x, y, text, pos, bbox_flag))
            except Exception:
                pass

        # vlines: x[, ymin, ymax][, linestyle][, color] (style/color any order)
        vline_vals: List[
            Tuple[float, float | None, float | None, str | None, str | None]
        ] = []
        _allowed_styles = {"solid", "dotted", "dashed", "dashdot"}
        for v in lists.get("vline", []):
            lit = _safe_literal(v)
            tokens: List[str] = []
            if isinstance(lit, (list, tuple)):
                tokens = [str(x).strip() for x in lit]
            else:
                tokens = [p.strip() for p in str(v).split(",") if p.strip()]

            nums: List[float] = []
            extras: List[str] = []
            for t in tokens:
                try:
                    nums.append(float(t))
                except Exception:
                    extras.append(t.lower())
            x_val: float | None = None
            y0_val: float | None = None
            y1_val: float | None = None
            if len(nums) >= 1:
                x_val = nums[0]
            if len(nums) >= 3:
                y0_val, y1_val = nums[1], nums[2]

            style: str | None = None
            color: str | None = None
            for e in extras:
                if e in _allowed_styles and style is None:
                    style = e
                elif color is None:
                    color = e
            if x_val is not None:
                vline_vals.append((x_val, y0_val, y1_val, style, color))

        # polygons: (x,y), (x,y), ... [ , show_vertices]
        # Parse without using literal_eval to avoid escape issues in labels.
        poly_vals: List[Tuple[List[Tuple[float, float]], bool]] = []
        num_re = r"[+-]?\d+(?:\.\d+)?"
        tup_pat = re.compile(rf"\(\s*({num_re})\s*,\s*({num_re})\s*\)")
        for p in lists.get("polygon", []):
            s = str(p).strip()
            # Remove an optional 'show_vertices' token (case-insensitive)
            show_vertices = False
            if re.search(r"(^|,)\s*show_vertices\s*(?=,|$)", s, flags=re.IGNORECASE):
                show_vertices = True
                s = re.sub(
                    r"(^|,)\s*show_vertices\s*(?=,|$)", ",", s, flags=re.IGNORECASE
                )
                s = re.sub(r",{2,}", ",", s).strip().strip(",")
            # Extract all (x,y) tuples
            pts: List[Tuple[float, float]] = []
            for m in tup_pat.finditer(s):
                try:
                    x = float(m.group(1))
                    y = float(m.group(2))
                    pts.append((x, y))
                except Exception:
                    pass
            if pts:
                poly_vals.append((pts, show_vertices))

        # bar: (x, y), length, orientation
        # Accept both literal list/tuple and CSV-like fallback
        bar_vals: List[Tuple[Tuple[float, float], float, str]] = []
        for b in lists.get("bar", []):
            lit = _safe_literal(b)
            if isinstance(lit, (list, tuple)) and len(lit) >= 3:
                try:
                    xy_raw, length_raw, orient_raw = lit[0], lit[1], lit[2]
                    xy = (float(xy_raw[0]), float(xy_raw[1]))
                    length = float(length_raw)
                    orientation = str(orient_raw).strip().lower()
                    if orientation in {"h", "hor", "horiz", "horizontal"}:
                        orientation = "horizontal"
                    elif orientation in {"v", "vert", "vertical"}:
                        orientation = "vertical"
                    bar_vals.append((xy, length, orientation))
                    continue
                except Exception:
                    pass
            # Fallback CSV: (x,y), length, orientation
            try:
                import csv as _csv

                s = str(b).strip()
                # Attempt to peel off the first tuple
                m = tup_pat.search(s)
                if not m:
                    continue
                x = float(m.group(1))
                y = float(m.group(2))
                # Remove tuple substring, then split the rest by commas
                a, c = m.span()
                rest = (s[:a] + s[c:]).strip()
                parts = [p.strip() for p in rest.split(",") if p.strip()]
                if len(parts) >= 2:
                    length = float(parts[0])
                    orientation = parts[1].strip().lower()
                    if orientation in {"h", "hor", "horiz", "horizontal"}:
                        orientation = "horizontal"
                    elif orientation in {"v", "vert", "vertical"}:
                        orientation = "vertical"
                    bar_vals.append(((x, y), length, orientation))
            except Exception:
                pass

        hline_vals: List[
            Tuple[float, float | None, float | None, str | None, str | None]
        ] = []
        for h in lists.get("hline", []):
            lit = _safe_literal(h)
            tokens_h: List[str] = []
            if isinstance(lit, (list, tuple)):
                tokens_h = [str(x).strip() for x in lit]
            else:
                tokens_h = [p.strip() for p in str(h).split(",") if p.strip()]

            nums_h: List[float] = []
            extras_h: List[str] = []
            for t in tokens_h:
                try:
                    nums_h.append(float(t))
                except Exception:
                    extras_h.append(t.lower())
            y_val: float | None = None
            x0_val: float | None = None
            x1_val: float | None = None
            if len(nums_h) >= 1:
                y_val = nums_h[0]
            if len(nums_h) >= 3:
                x0_val, x1_val = nums_h[1], nums_h[2]

            style_h: str | None = None
            color_h: str | None = None
            for e in extras_h:
                if e in _allowed_styles and style_h is None:
                    style_h = e
                elif color_h is None:
                    color_h = e
            if y_val is not None:
                hline_vals.append((y_val, x0_val, x1_val, style_h, color_h))

        # lines: a, b, color, linestyle OR a, (x, y), color, linestyle
        # color and linestyle optional and order-independent; linestyle defaults to dashed
        line_vals: List[Tuple[float, float, str | None, str | None]] = (
            []
        )  # (a, b, style, color)
        _allowed_styles_line = {"solid", "dotted", "dashed", "dashdot"}

        def _split_top_level_line(val: str) -> List[str]:
            s = str(val or "").strip()
            if not s:
                return []
            if (s.startswith("[") and s.endswith("]")) or (
                s.startswith("(") and s.endswith(")")
            ):
                s = s[1:-1].strip()
            out: List[str] = []
            cur: List[str] = []
            depth = 0
            for ch in s:
                if ch in "([{":
                    depth += 1
                    cur.append(ch)
                elif ch in ")]}":
                    depth = max(0, depth - 1)
                    cur.append(ch)
                elif ch == "," and depth == 0:
                    part = "".join(cur).strip()
                    if part:
                        out.append(part)
                    cur = []
                else:
                    cur.append(ch)
            tail = "".join(cur).strip()
            if tail:
                out.append(tail)
            return out

        num_re_line = r"[+-]?\d+(?:\.\d+)?"
        tup_pat_line = re.compile(rf"\(\s*({num_re_line})\s*,\s*({num_re_line})\s*\)")
        for l in lists.get("line", []):
            a_val: float | None = None
            b_val: float | None = None
            style_line: str | None = None
            color_line: str | None = None
            lit_line = _safe_literal(l)
            if isinstance(lit_line, (list, tuple)) and len(lit_line) >= 2:
                try:
                    a_val = float(lit_line[0])
                except Exception:
                    a_val = None
                second = lit_line[1]
                if isinstance(second, (list, tuple)) and len(second) == 2:
                    try:
                        x0p = float(second[0])
                        y0p = float(second[1])
                        if a_val is not None:
                            b_val = y0p - a_val * x0p
                    except Exception:
                        pass
                else:
                    try:
                        b_val = float(second)
                    except Exception:
                        pass
                for extra in list(lit_line[2:]):
                    if isinstance(extra, str):
                        e = extra.strip().strip("\"'")
                        if e.lower() in _allowed_styles_line and style_line is None:
                            style_line = e.lower()
                        elif color_line is None:
                            color_line = e
                if a_val is not None and b_val is not None:
                    line_vals.append((a_val, b_val, style_line, color_line))
                    continue
            parts = _split_top_level_line(str(l))
            if len(parts) >= 2:
                try:
                    a_val = float(parts[0])
                except Exception:
                    a_val = None
                mpt = tup_pat_line.match(parts[1])
                if mpt is not None:
                    try:
                        x0p = float(mpt.group(1))
                        y0p = float(mpt.group(2))
                        if a_val is not None:
                            b_val = y0p - a_val * x0p
                    except Exception:
                        pass
                else:
                    try:
                        b_val = float(parts[1])
                    except Exception:
                        pass
                for extra in parts[2:]:
                    e = str(extra).strip().strip("\"'")
                    if e.lower() in _allowed_styles_line and style_line is None:
                        style_line = e.lower()
                    elif color_line is None:
                        color_line = e
                if a_val is not None and b_val is not None:
                    line_vals.append((a_val, b_val, style_line, color_line))

        # fill-polygons: (x,y), (x,y), ... [, color] [, alpha]
        # Defaults: color -> plotmath.COLORS.get("blue"), alpha -> 0.1
        poly_fill_vals: List[
            Tuple[List[Tuple[float, float]], str | None, float | None]
        ] = []
        for fp in lists.get("fill-polygon", []):
            s = str(fp).strip()
            # Extract all (x,y) tuples
            pts_fp: List[Tuple[float, float]] = []
            matches = list(tup_pat.finditer(s))
            for m in matches:
                try:
                    pts_fp.append((float(m.group(1)), float(m.group(2))))
                except Exception:
                    pass
            # Remove the tuple substrings to parse remaining tokens as extras
            rest = s
            for m in reversed(matches):
                a, b = m.span()
                rest = rest[:a] + rest[b:]
            rest = re.sub(r",{2,}", ",", rest)
            extras = [tok.strip() for tok in rest.split(",") if tok.strip()]
            color_fp: str | None = None
            alpha_fp: float | None = None
            # Interpret extras in any order: first numeric -> alpha, first non-numeric -> color
            for tok in extras:
                if alpha_fp is None:
                    try:
                        alpha_fp = float(tok)
                        continue
                    except Exception:
                        pass
                if color_fp is None:
                    color_fp = tok
                # Stop early if both parsed
                if color_fp is not None and alpha_fp is not None:
                    break
            if pts_fp:
                poly_fill_vals.append((pts_fp, color_fp, alpha_fp))

        # axis commands: allow repeated keys like axis: equal / axis: off
        axis_cmds: List[str] = []
        for a in lists.get("axis", []):
            s = str(a).strip()
            # Allow comma-separated in one line as a convenience
            parts = [part.strip() for part in s.split(",") if part.strip()]
            for part in parts:
                # strip optional quotes
                if (part.startswith("'") and part.endswith("'")) or (
                    part.startswith('"') and part.endswith('"')
                ):
                    part = part[1:-1].strip()
                if part:
                    axis_cmds.append(part)

        explicit_name = merged.get("name")
        debug_mode = "debug" in merged

        # Hash includes all content affecting the image
        content_hash = _hash_key(
            "|".join(fn_exprs),
            "|".join(fn_labels_list),
            "|".join(["" if d is None else f"{d[0]},{d[1]}" for d in fn_domains_list]),
            "|".join([("|".join([str(x) for x in exs])) for exs in fn_exclusions_list]),
            ";".join([f"{x},{y}" for x, y in point_vals]),
            ";".join(
                [
                    f"{xt[0]},{xt[1]}->{xy[0]},{xy[1]}:{t}:{arc}"
                    for (xt, xy, t, arc) in ann_vals
                ]
            ),
            ";".join(
                [
                    (f"{x}" if y0 is None or y1 is None else f"{x},{y0},{y1}")
                    + f":{st or ''}:{col or ''}"
                    for (x, y0, y1, st, col) in vline_vals
                ]
            ),
            ";".join(
                [
                    (f"{y}" if x0 is None or x1 is None else f"{y},{x0},{x1}")
                    + f":{st or ''}:{col or ''}"
                    for (y, x0, x1, st, col) in hline_vals
                ]
            ),
            ";".join(
                [
                    f"{int(show)}:" + "|".join([f"{x},{y}" for (x, y) in pts])
                    for (pts, show) in poly_vals
                ]
            ),
            ";".join(
                [
                    (color or "")
                    + ":"
                    + ("" if alpha is None else str(alpha))
                    + ":"
                    + "|".join([f"{x},{y}" for (x, y) in pts])
                    for (pts, color, alpha) in poly_fill_vals
                ]
            ),
            ";".join(
                [
                    f"{xy[0]},{xy[1]}:{length}:{orientation}"
                    for (xy, length, orientation) in bar_vals
                ]
            ),
            "|".join(axis_cmds),
            ";".join(
                [f"{a},{b}:{(st or '')}:{(col or '')}" for (a, b, st, col) in line_vals]
            ),
            ";".join(
                [
                    f"{x},{y}:{txt}:{pos}:{int(1 if bbox else 0)}"
                    for (x, y, txt, pos, bbox) in text_vals
                ]
            ),
            xmin,
            xmax,
            ymin,
            ymax,
            xstep,
            ystep,
            fontsize,
            lw,
            alpha,
            str(merged.get("xlabel", "")),
            str(merged.get("ylabel", "")),
            int(bool(ticks_flag)),
            int(bool(grid_flag)),
        )
        base_name = explicit_name or f"plot_{content_hash}"

        rel_dir = os.path.join("_static", "plot")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        if regenerate:
            import matplotlib

            matplotlib.use("Agg")
            try:
                # Create bare axes using plotmath.plot with no functions
                fig, ax = plotmath.plot(
                    functions=[],
                    fn_labels=False,
                    xmin=xmin,
                    xmax=xmax,
                    ymin=ymin,
                    ymax=ymax,
                    xstep=xstep,
                    ystep=ystep,
                    ticks=ticks_flag,
                    grid=grid_flag,
                    lw=lw,
                    alpha=alpha,
                    fontsize=fontsize,
                )

                # Plot requested functions directly on ax, with optional labels, per-function domains, and exclusions
                if functions:
                    import numpy as np

                    any_label = False
                    for f, lbl, dom, exs in zip(
                        functions, fn_labels_list, fn_domains_list, fn_exclusions_list
                    ):
                        x0, x1 = dom if dom is not None else (xmin, xmax)
                        N = int(2**12)
                        x = np.linspace(x0, x1, N)
                        y = f(x)
                        # Ensure float array and blank out non-finite values
                        y = np.asarray(y, dtype=float)
                        y[~np.isfinite(y)] = np.nan
                        # More robust exclusion handling: blank a window around each excluded x
                        exs_in = [e for e in exs if x0 < e < x1]
                        if exs_in and N > 1:
                            dx = (x1 - x0) / (N - 1)
                            # Window width larger than step to ensure a gap; include tiny absolute floor
                            w = max(4 * dx, 1e-6 * (1.0 + max(abs(e) for e in exs_in)))
                            for e in exs_in:
                                try:
                                    mask = np.abs(x - e) <= w
                                    if mask.any():
                                        y[mask] = np.nan
                                    # Also blank the nearest index and a couple of neighbors to guarantee a break
                                    j = int(np.argmin(np.abs(x - e)))
                                    for k in (j - 2, j - 1, j, j + 1, j + 2):
                                        if 0 <= k < y.size:
                                            y[k] = np.nan
                                except Exception:
                                    # Last resort: nearest index only
                                    try:
                                        j = int(np.argmin(np.abs(x - e)))
                                        if 0 <= j < y.size:
                                            y[j] = np.nan
                                    except Exception:
                                        pass
                        # Additionally, break lines across steep jumps or extreme values
                        # Determine a reasonable y-span for thresholds
                        y_span = (
                            abs(ymax - ymin)
                            if (ymax is not None and ymin is not None)
                            else np.nan
                        )
                        if not (isinstance(y_span, (int, float)) and y_span > 0):
                            finite_y = y[np.isfinite(y)]
                            if finite_y.size > 0:
                                y_span = float(
                                    np.nanmax(finite_y) - np.nanmin(finite_y)
                                )
                        if not (isinstance(y_span, (int, float)) and y_span > 0):
                            y_span = 1.0
                        # Break where adjacent points jump too much relative to span
                        jump_factor = 0.5  # half the axis span signals discontinuity
                        finite_pair = np.isfinite(y[:-1]) & np.isfinite(y[1:])
                        big_jump = finite_pair & (
                            np.abs(y[1:] - y[:-1]) > (jump_factor * y_span)
                        )
                        if big_jump.any():
                            idx_break = np.where(big_jump)[0]
                            for i_b in idx_break:
                                if 0 <= i_b + 1 < y.size:
                                    y[i_b + 1] = np.nan
                        # Mask values far outside typical range to avoid vertical spikes drawing across
                        mag_factor = 50.0
                        too_big = np.isfinite(y) & (np.abs(y) > (mag_factor * y_span))
                        if too_big.any():
                            y[too_big] = np.nan
                        if lbl:
                            any_label = True
                            ax.plot(x, y, lw=lw, alpha=alpha, label=f"${lbl}$")
                        else:
                            ax.plot(x, y, lw=lw, alpha=alpha)
                    if any_label:
                        ax.legend(fontsize=int(fontsize))

                # Annotations
                for xytext, xy, text, arc in ann_vals:
                    plotmath.annotate(
                        xy=xy, xytext=xytext, s=text, arc=arc, fontsize=int(fontsize)
                    )

                # Lines (y = a*x + b); draw before points so markers remain visible
                if line_vals:
                    import numpy as _np_l

                    style_map_line = {
                        "solid": "-",
                        "dotted": ":",
                        "dashed": "--",
                        "dashdot": "-.",
                    }
                    default_color_line = plotmath.COLORS.get("red")
                    try:
                        from matplotlib import colors as _mcolors
                    except Exception:
                        _mcolors = None
                    x_line = _np_l.array([xmin, xmax], dtype=float)
                    for a_l, b_l, st_l, col_l in line_vals:
                        y_line = a_l * x_line + b_l
                        ls = style_map_line.get((st_l or "dashed").lower(), "--")
                        col_use = col_l or default_color_line
                        if _mcolors is not None:
                            try:
                                _ = _mcolors.to_rgba(col_use)
                            except Exception:
                                col_use = default_color_line
                        try:
                            ax.plot(
                                x_line,
                                y_line,
                                linestyle=ls,
                                color=col_use,
                                lw=lw,
                                alpha=alpha,
                            )
                        except Exception:
                            ax.plot(
                                x_line,
                                y_line,
                                linestyle=ls,
                                color=default_color_line,
                                lw=lw,
                                alpha=alpha,
                            )

                # Plot points
                for x0, y0 in point_vals:
                    ax.plot(x0, y0, "o", markersize=10, alpha=0.8, color="black")

                # Bars
                for xy, length, orientation in bar_vals:
                    try:
                        # Prefer plotmath.make_bar if available
                        if hasattr(plotmath, "make_bar"):
                            plotmath.make_bar(xy, length, orientation)
                        else:
                            # Fallback: use annotate directly on this axes
                            x, y = xy
                            if orientation == "horizontal":
                                ax.annotate(
                                    "",
                                    xy=xy,
                                    xycoords="data",
                                    xytext=(x + length, y),
                                    textcoords="data",
                                    arrowprops=dict(
                                        arrowstyle="|-|,widthA=0.5,widthB=0.5",
                                        color="black",
                                    ),
                                )
                            else:
                                ax.annotate(
                                    "",
                                    xy=xy,
                                    xycoords="data",
                                    xytext=(x, y + length),
                                    textcoords="data",
                                    arrowprops=dict(
                                        arrowstyle="|-|,widthA=0.5,widthB=0.5",
                                        color="black",
                                    ),
                                )
                    except Exception:
                        pass

                # text with optional positioning and optional bbox

                xmin, xmax = ax.get_xlim()
                ymin, ymax = ax.get_ylim()
                ax_dx = xmax - xmin
                ax_dy = ymax - ymin

                # Determine axes pixel size for consistent visual offsets
                try:
                    fig.canvas.draw()  # ensure layout is realized
                    _bbox_px = ax.get_window_extent()
                    _ax_w_px, _ax_h_px = _bbox_px.width, _bbox_px.height
                    if _ax_w_px <= 0 or _ax_h_px <= 0:
                        _ax_w_px = _ax_h_px = None
                except Exception:
                    _ax_w_px = _ax_h_px = None

                for x0, y0, text, pos, use_bbox in text_vals:
                    va, ha = _parse_text_positioning(pos)
                    # Factors as fractions of axes size; keep long* ~3.3x larger
                    _fx_short = 0.015
                    _fy_short = 0.015
                    _fx_long = 0.03
                    _fy_long = 0.03

                    # Resolve long* into base alignment while keeping larger factors
                    _use_fx = _fx_short
                    _use_fy = _fy_short
                    if va == "longbottom":
                        va = "bottom"
                        _use_fy = _fy_long
                    elif va == "longtop":
                        va = "top"
                        _use_fy = _fy_long
                    if ha == "longright":
                        ha = "right"
                        _use_fx = _fx_long
                    elif ha == "longleft":
                        ha = "left"
                        _use_fx = _fx_long

                    if _ax_w_px and _ax_h_px:
                        # Pixel-based offsets converted back to data units
                        dx_px = 0.0
                        dy_px = 0.0
                        if ha == "right":
                            dx_px = -_ax_w_px * _use_fx
                        elif ha == "left":
                            dx_px = _ax_w_px * _use_fx
                        if va == "bottom":
                            dy_px = _ax_h_px * _use_fy
                        elif va == "top":
                            dy_px = -_ax_h_px * _use_fy
                        x_disp, y_disp = ax.transData.transform((x0, y0))
                        x1, y1 = ax.transData.inverted().transform(
                            (x_disp + dx_px, y_disp + dy_px)
                        )
                        dx = x1 - x0
                        dy = y1 - y0
                    else:
                        # Fallback to fractions of data span
                        if va == "bottom":
                            dy = (
                                _fy_short * ax_dy
                                if _use_fy == _fy_short
                                else _fy_long * ax_dy
                            )
                        elif va == "top":
                            dy = -(
                                _fy_short * ax_dy
                                if _use_fy == _fy_short
                                else _fy_long * ax_dy
                            )
                        else:
                            dy = 0.0
                        if ha == "right":
                            dx = -(
                                _fx_short * ax_dx
                                if _use_fx == _fx_short
                                else _fx_long * ax_dx
                            )
                        elif ha == "left":
                            dx = (
                                _fx_short * ax_dx
                                if _use_fx == _fx_short
                                else _fx_long * ax_dx
                            )
                        else:
                            dx = 0.0

                    bbox_kwargs = (
                        dict(
                            boxstyle="round,pad=0.4",
                            fc="white",
                            ec="black",
                            lw=1.5,
                            alpha=0.7,
                        )
                        if use_bbox
                        else None
                    )

                    if bbox_kwargs:
                        ax.text(
                            x0 + 1.5 * dx,
                            y0 + 1.5 * dy,
                            text,
                            fontsize=int(fontsize),
                            ha=ha,
                            va=va,
                            bbox=bbox_kwargs,
                        )
                    else:
                        ax.text(
                            x0 + dx, y0 + dy, text, fontsize=int(fontsize), ha=ha, va=va
                        )

                # vlines
                style_map = {
                    "solid": "-",
                    "dotted": ":",
                    "dashed": "--",
                    "dashdot": "-.",
                }
                default_color = plotmath.COLORS.get("red")
                for x_v, y0, y1, st, col in vline_vals:
                    y_min = ymin if y0 is None else y0
                    y_max = ymax if y1 is None else y1
                    ls_val = style_map.get((st or "dotted").lower(), ":")
                    color_to_try = col if col else default_color
                    try:
                        ax.vlines(
                            x=x_v,
                            ymin=y_min,
                            ymax=y_max,
                            colors=color_to_try,
                            lw=lw,
                            alpha=1,
                            ls=ls_val,
                        )
                    except Exception:
                        ax.vlines(
                            x=x_v,
                            ymin=y_min,
                            ymax=y_max,
                            colors=default_color,
                            lw=lw,
                            alpha=1,
                            ls=ls_val,
                        )

                # hlines
                for y_h, x0, x1, st_h, col_h in hline_vals:
                    x_min = xmin if x0 is None else x0
                    x_max = xmax if x1 is None else x1
                    ls_val_h = style_map.get((st_h or "dotted").lower(), ":")
                    color_to_try_h = col_h if col_h else default_color
                    try:
                        ax.hlines(
                            y=y_h,
                            xmin=x_min,
                            xmax=x_max,
                            colors=color_to_try_h,
                            lw=lw,
                            alpha=1,
                            ls=ls_val_h,
                        )
                    except Exception:
                        ax.hlines(
                            y=y_h,
                            xmin=x_min,
                            xmax=x_max,
                            colors=default_color,
                            lw=lw,
                            alpha=1,
                            ls=ls_val_h,
                        )

                # polygons
                for pts, show in poly_vals:
                    kwargs = {"show_vertices": True} if show else {}
                    try:
                        plotmath.polygon(*pts, **kwargs)
                    except Exception:
                        # ignore to avoid breaking the build on a single bad polygon
                        pass

                # filled polygons
                default_fill_color = plotmath.COLORS.get("blue")
                for pts, color_fp, alpha_fp in poly_fill_vals:
                    c = color_fp or default_fill_color
                    a = 0.1 if alpha_fp is None else alpha_fp
                    try:
                        plotmath.polygon(*pts, edges=False, color=c, alpha=a)
                    except Exception:
                        try:
                            plotmath.polygon(*pts, edges=False, facecolor=c, alpha=a)
                        except Exception:
                            plotmath.polygon(*pts, edges=False, alpha=a)

                # axis commands (run sequentially)
                for cmd in axis_cmds:
                    try:
                        ax.axis(cmd)
                    except Exception:
                        pass

                # Axis labels
                xl_text = merged.get("xlabel")
                yl_text = merged.get("ylabel")
                if isinstance(yl_text, str) and yl_text.strip():
                    try:
                        ax.set_ylabel(
                            f"${yl_text}$",
                            fontsize=int(fontsize),
                            loc="top",
                            rotation="horizontal",
                        )
                    except Exception:
                        ax.set_ylabel(yl_text, fontsize=int(fontsize))
                if isinstance(xl_text, str) and xl_text.strip():
                    try:
                        ax.set_xlabel(
                            f"${xl_text}$",
                            fontsize=int(fontsize),
                            loc="right",
                        )
                    except Exception:
                        ax.set_xlabel(xl_text, fontsize=int(fontsize))

                fig.savefig(
                    abs_svg, format="svg", bbox_inches="tight", transparent=True
                )
                if debug_mode:
                    # Sidecar PDF (optional for debugging)
                    try:
                        fig.savefig(
                            os.path.join(abs_dir, f"{base_name}.pdf"),
                            format="pdf",
                            bbox_inches="tight",
                            transparent=True,
                        )
                    except Exception:
                        pass

                matplotlib.pyplot.close(fig)
            except Exception as e:
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av figur: {e}", line=self.lineno
                    )
                ]

        if not os.path.exists(abs_svg):
            return [
                self.state_machine.reporter.error(
                    "plot: SVG mangler.", line=self.lineno
                )
            ]

        env.note_dependency(abs_svg)
        # copy into build _static
        try:
            out_static = os.path.join(app.outdir, "_static", "plot")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"plot inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

        if not debug_mode and "viewBox" in raw_svg:
            raw_svg = _strip_root_svg_size(raw_svg)

        if not debug_mode:
            raw_svg = _rewrite_ids(
                raw_svg, f"cpl_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = "Tilpasset figur"
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
            ["adaptive-figure", "plot-figure", "no-click"]
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

        if explicit_name:
            self.add_name(figure)
        return [figure]


def setup(app):  # pragma: no cover
    app.add_directive("plot", PlotDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
