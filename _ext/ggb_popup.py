from docutils import nodes
from sphinx.util.docutils import SphinxDirective
import uuid


class GGBPopUpDirective(SphinxDirective):
    required_arguments = 0
    optional_arguments = 4  # width, height, button text, dialog title
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        "layout": lambda arg: arg,  # e.g., "sidebar"
        "menubar": lambda arg: arg,  # e.g., "true" or "false"
        "perspective": lambda arg: arg,  # e.g., "GS"
    }

    def run(self):
        # 1 » parse args -----------------------------------------------------
        width = int(self.arguments[0]) if len(self.arguments) > 0 else 700
        height = int(self.arguments[1]) if len(self.arguments) > 1 else 500

        button_text = (
            self.arguments[2] if len(self.arguments) > 2 else "Åpne Geogebra‑vindu"
        )
        dialog_title = (
            self.arguments[3] if len(self.arguments) > 3 else "Geogebra‑vindu"
        )

        menubar = self.options.get("menubar", "false")

        perspective = self.options.get("perspective", "AG").strip()

        # 2 » unique IDs -----------------------------------------------------
        cid = f"ggb-geogebra-{uuid.uuid4().hex[:8]}"
        dialog_id = f"dialog-{cid}"
        button_id = f"button-{cid}"

        # 3 » layout option --------------------------------------------------
        layout = self.options.get("layout", "").strip().lower()
        use_sidebar = layout == "sidebar"

        wrapper_start = '<div class="sidebar-cas">' if use_sidebar else ""
        wrapper_end = "</div>" if use_sidebar else ""

        # 4 » HTML content ---------------------------------------------------
        html = f"""
{wrapper_start}
<meta name="viewport" content="width=device-width, initial-scale=1">

<button id="{button_id}" class="ggb-cas-button">{button_text}</button>
<div id="{dialog_id}" title="{dialog_title}" style="display:none;">
    <div id="{cid}" class="ggb-window"></div>
</div>

<style>
.ui-resizable-handle {{ min-width:16px;min-height:16px; }}
.ui-dialog-content{{padding:0!important;}}
.ggb-window       {{width:100%!important;height:100%!important;box-sizing:border-box;}}
.ggb-cas-button   {{margin-top: 1em; margin-bottom: 1em;}}
</style>

<script>
(function() {{
  $(function() {{
    let ggbReady = false;

    function applySize() {{
      if (!ggbReady) return;
      const w = $("#{cid}").width(),
            h = $("#{cid}").height();
      window.ggbApplet.setSize(Math.round(w), Math.round(h));
    }}

    $("#{dialog_id}").dialog({{
      autoOpen: false,
      width: {width+40}, height: {height+80},
      resizable: true, draggable: true,
      position: {{ my: "center", at: "center", of: window }},
      resize: () => window.requestAnimationFrame(applySize),
      open: function() {{
        if (!ggbReady) {{
          new GGBApplet({{
            appName: "classic", id: "{cid}",
            width: {width}, height: {height},
            perspective: "{perspective}", language: "nb",
            showToolBar: true, showAlgebraInput: true,
            borderRadius: 8, enableRightClick: true, showKeyboardOnFocus: false,
            showMenuBar: {menubar},
            appletOnLoad: () => {{ ggbReady = true; applySize(); }}
          }}, true).inject("{cid}");
        }} else {{
          applySize();
        }}
      }}
    }});

    $("#{button_id}").button()
      .on("click touchend pointerup", e => {{
        e.preventDefault();
        $("#{dialog_id}").dialog("open");
      }});
  }});
}})();
</script>
{wrapper_end}
        """
        return [nodes.raw("", html, format="html")]


def setup(app):
    app.add_directive("ggb-popup", GGBPopUpDirective)
    app.add_css_file("misc_styles/cas_popup.css")
    return {"version": "0.4", "parallel_read_safe": True, "parallel_write_safe": True}
