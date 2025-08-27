import os
import shutil
import hashlib
import re
import uuid
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


def _hash_key(*parts):
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


class PolyDivDirective(SphinxDirective):
    """Generate (and cache) a polynomial long division figure as SVG and embed it.

    Usage (MyST):

    ````
    ::::{polydiv}
    :p: x^3 + 2x^2 - 3x - 6
    :q: x - 2
    :stage: 2        # optional
    :vars: x         # optional (default x)
    :align: center   # optional (left|center|right)
    :class: small    # optional extra CSS classes on figure

    Valgfri bildetekst her.
    ::::
    ````

    Or classic reStructuredText:

    .. polydiv::
       :p: x^3 + 2x^2 - 3x - 6
       :q: x - 2
       :stage: 2
       :vars: x

       Valgfri bildetekst her.
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "p": directives.unchanged_required,
        "q": directives.unchanged_required,
        "stage": directives.nonnegative_int,
        "vars": directives.unchanged,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,  # optional explicit base filename / ref name
        "cache": directives.flag,  # include to enable (default on)
        "nocache": directives.flag,  # include to force regeneration
        "alt": directives.unchanged,
        "width": directives.length_or_percentage_or_unitless,
        # Always inline now; legacy 'inline' option kept (ignored) for backward compatibility
        "inline": directives.flag,
    }

    def run(self):
        """Main directive entry: always inline-embed generated SVG and allow width control & centering."""
        env = self.state.document.settings.env
        app = env.app

        try:
            from python_util.polydiv import polylongdiv
        except Exception as e:  # pragma: no cover
            msg = nodes.error()
            msg += nodes.paragraph(text=f"Kunne ikke importere polydiv-modulen: {e}")
            return [msg]

        # Options
        p = self.options.get("p")
        q = self.options.get("q")
        if p is None or q is None:
            return [
                self.state_machine.reporter.error(
                    "Directive 'polydiv' krever både :p: og :q: opsjoner.",
                    line=self.lineno,
                )
            ]
        stage = self.options.get("stage")
        vars_opt = self.options.get("vars", "x")
        explicit_name = self.options.get("name")
        content_hash = _hash_key(p, q, stage, vars_opt)
        base_name = explicit_name or f"polydiv_{content_hash}"

        # Paths
        src_dir = app.srcdir
        rel_dir = os.path.join("_static", "polydiv")
        abs_dir = os.path.join(src_dir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_filename = f"{base_name}.svg"
        abs_svg_path = os.path.join(abs_dir, svg_filename)

        regenerate = "nocache" in self.options or not os.path.exists(abs_svg_path)
        if regenerate:
            cwd = os.getcwd()
            try:
                os.chdir(abs_dir)
                polylongdiv(
                    fname=base_name,
                    p=p,
                    q=q,
                    stage=stage,
                    vars=vars_opt,
                )
            except Exception as e:  # pragma: no cover
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av polynomdivisjon: {e}",
                        line=self.lineno,
                    )
                ]
            finally:
                os.chdir(cwd)

        # Post-process: strip width/height for responsiveness if viewBox present
        try:
            if os.path.exists(abs_svg_path):
                with open(abs_svg_path, "r", encoding="utf-8") as f_svg:
                    svg_text_tmp = f_svg.read()
                if "viewBox" in svg_text_tmp:
                    cleaned = re.sub(r'\swidth="[^"]+"', "", svg_text_tmp)
                    cleaned = re.sub(r'\sheight="[^"]+"', "", cleaned)
                    if cleaned != svg_text_tmp:
                        with open(abs_svg_path, "w", encoding="utf-8") as f_out:
                            f_out.write(cleaned)
        except Exception:
            pass

        if not os.path.exists(abs_svg_path):
            return [
                self.state_machine.reporter.error(
                    (
                        f"polydiv: klarte ikke å generere SVG '{svg_filename}'. "
                        "Kontroller at 'pdflatex' og 'pdf2svg' er installert i miljøet."
                    ),
                    line=self.lineno,
                )
            ]

        env.note_dependency(abs_svg_path)
        try:
            out_static = os.path.join(app.outdir, "_static", "polydiv")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg_path, os.path.join(out_static, svg_filename))
        except Exception:
            pass

        # Alt text
        if stage is not None:
            default_alt = f"Polynomdivisjon av ({p}) : ({q}) – trinn {stage}"
        else:
            default_alt = f"Polynomdivisjon av ({p}) : ({q})"
        alt = self.options.get("alt", default_alt)

        width_opt = self.options.get("width")
        percentage_width = isinstance(width_opt, str) and width_opt.strip().endswith(
            "%"
        )

        # Read final SVG
        try:
            with open(abs_svg_path, "r", encoding="utf-8") as f_svg:
                raw_svg = f_svg.read()
        except Exception as e:  # pragma: no cover
            return [
                self.state_machine.reporter.error(
                    f"polydiv inline: kunne ikke lese SVG: {e}",
                    line=self.lineno,
                )
            ]

        # Uniquify IDs to prevent collisions
        def _uniquify_ids(svg_text: str, prefix: str) -> str:
            ids = set(re.findall(r'\bid="([^"]+)"', svg_text))
            if not ids:
                return svg_text
            mapping = {old: f"{prefix}{old}" for old in ids}
            for old, new in mapping.items():
                svg_text = re.sub(rf'\bid="{re.escape(old)}"', f'id="{new}"', svg_text)
            for old, new in mapping.items():
                svg_text = re.sub(
                    rf'(?:xlink:)?href="#?{re.escape(old)}"', f'href="#{new}"', svg_text
                )
                svg_text = re.sub(
                    rf'xlink:href="#?{re.escape(old)}"',
                    f'xlink:href="#{new}"',
                    svg_text,
                )
            for old, new in mapping.items():
                svg_text = re.sub(
                    rf"url\(#\s*{re.escape(old)}\s*\)", f"url(#{new})", svg_text
                )
            for old, new in mapping.items():
                svg_text = re.sub(rf"#({re.escape(old)})\b", f"#{new}", svg_text)
            return svg_text

        unique_prefix = f"pd_{_hash_key(p, q, stage, vars_opt)}_{uuid.uuid4().hex[:6]}_"
        raw_svg = _uniquify_ids(raw_svg, unique_prefix)

        # Augment root <svg>
        def _augment(match):
            tag = match.group(0)
            if "class=" not in tag:
                tag = tag[:-1] + ' class="polydiv-inline-svg"' + ">"
            else:
                tag = tag.replace('class="', 'class="polydiv-inline-svg ')
            if alt and "aria-label=" not in tag:
                tag = tag[:-1] + f' role="img" aria-label="{alt}"' + ">"
            # For percentage width, apply exact percentage to SVG
            if percentage_width and width_opt:
                percent_val = width_opt.strip()
                # add helper class
                if "polydiv-fill" not in tag:
                    if "class=" in tag:
                        tag = tag.replace('class="', 'class="polydiv-fill ')
                    else:
                        tag = tag[:-1] + ' class="polydiv-fill"' + ">"
                if "style=" in tag:
                    tag = re.sub(
                        r'style="([^"]*)"',
                        lambda m: f'style="{m.group(1)}; width:{percent_val}; height:auto; display:block; margin:0 auto;"',
                        tag,
                        count=1,
                    )
                else:
                    tag = (
                        tag[:-1]
                        + f' style="width:{percent_val}; height:auto; display:block; margin:0 auto;"'
                        + ">"
                    )
            return tag

        raw_svg = re.sub(r"<svg\b[^>]*>", _augment, raw_svg, count=1)
        if alt and "<title" not in raw_svg:
            raw_svg = re.sub(
                r"(<svg\b[^>]*>)",
                r"\1<title>" + re.escape(alt) + r"</title>",
                raw_svg,
                count=1,
            )

        # Apply explicit width (non-percent) directly to svg
        if width_opt and not percentage_width:

            def _apply_width(match):
                tag = match.group(0)
                w_val = width_opt.strip()
                w_css = (w_val + "px") if w_val.isdigit() else w_val
                if "style=" in tag:
                    tag = re.sub(
                        r'style="([^"]*)"',
                        lambda m: f'style="{m.group(1)}; width:{w_css}; height:auto;"',
                        tag,
                        count=1,
                    )
                else:
                    tag = tag[:-1] + f' style="width:{w_css}; height:auto;"' + ">"
                return tag

            raw_svg = re.sub(r"<svg\b[^>]*>", _apply_width, raw_svg, count=1)

        figure = nodes.figure()
        figure.setdefault("classes", []).extend(
            [
                "adaptive-figure",
                "polydiv-figure",
                "no-click",
            ]
        )
        # Do not set figure width for percentage; SVG carries explicit percent, allowing centering.

        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            [
                "polydiv-image",
                "no-click",
                "no-scaled-link",
            ]
        )
        figure += raw_node

        # Extra classes & alignment
        extra_classes = self.options.get("class")
        if extra_classes:
            figure["classes"].extend(extra_classes)
        figure["align"] = self.options.get("align", "center")

        # Caption
        if self.content:
            caption_text = "\n".join(self.content)
            caption_node = nodes.caption()
            caption_node += nodes.Text(caption_text)
            figure += caption_node

        if explicit_name:
            self.add_name(figure)

        return [figure]


def setup(app):
    app.add_directive("polydiv", PolyDivDirective)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
