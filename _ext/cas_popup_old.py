from docutils import nodes
from sphinx.util.docutils import SphinxDirective
import uuid


class CASPopUpDirective(SphinxDirective):
    required_arguments = 0  # width, height
    optional_arguments = 4  # width, height, button text, dialog title
    has_content = False

    def run(self):
        # 1 » parse args -----------------------------------------------------
        width = int(self.arguments[0]) if len(self.arguments) > 0 else 350
        height = int(self.arguments[1]) if len(self.arguments) > 1 else 500

        button_text = self.arguments[2] if len(self.arguments) > 2 else "Åpne CAS‑vindu"
        dialog_title = self.arguments[3] if len(self.arguments) > 3 else "CAS‑vindu"

        # 2 » unique IDs -----------------------------------------------------
        cid = f"ggb-cas-{uuid.uuid4().hex[:8]}"
        dialog_id = f"dialog-{cid}"
        button_id = f"button-{cid}"

        # 3 » HTML / CSS / JS ----------------------------------------------
        html = f"""
<meta name="viewport" content="width=device-width, initial-scale=1">


<button id="{button_id}" class="ggb-cas-button">{button_text}</button>
<div id="{dialog_id}" title="{dialog_title}" style="display:none;">
    <!-- ✨ inline width/height REMOVED so CSS can take over -->
    <div id="{cid}" class="ggb-window"></div>
</div>

<style>
.ui-resizable-handle {{ min-width:16px;min-height:16px; }}
/* kill jQuery‑UI’s 10 px padding & let the CAS pane fill the box */
.ui-dialog-content{{padding:0!important;}}
.ggb-window       {{width:100%!important;height:100%!important;box-sizing:border-box;}}
.ggb-cas-button   {{margin-top: 1em; margin-bottom: 1em;}}
</style>

<script>
(function() {{
  $(function() {{
    let ggbReady = false;

    function applySize(){{
      if(!ggbReady) return;
      const w = $("#{cid}").width(),
            h = $("#{cid}").height();
      window.ggbApplet.setSize(Math.round(w), Math.round(h));
    }}

    $("#{dialog_id}").dialog({{
      autoOpen:false,
      width:{width+40},height:{height+80},
      resizable:true,draggable:true,
      position:{{my:"center",at:"center",of:window}},
      resize:()=>window.requestAnimationFrame(applySize),
      open:function(){{
        if(!ggbReady){{
          new GGBApplet({{
            appName:"classic",id:"{cid}",
            width:{width},height:{height},
            perspective:"C",language:"nb",
            showToolBar:true,showAlgebraInput:true,
            borderRadius:8,enableRightClick:true,showKeyboardOnFocus:false,
            customToolBar:"1001 | 1002 | 1007 | 1010 | 6",
            appletOnLoad:()=>{{ggbReady=true;applySize();}}
          }},true).inject("{cid}");
        }}else{{applySize();}}
      }}
    }});

    $("#{button_id}").button()
      .on("click touchend pointerup",e=>{{e.preventDefault();$("#{dialog_id}").dialog("open");}});
  }});
}})();
</script>
        """
        return [nodes.raw("", html, format="html")]


def setup(app):
    app.add_directive("cas-popup", CASPopUpDirective)
    app.add_css_file("misc_styles/cas_popup.css")
    return {"version": "0.4", "parallel_read_safe": True, "parallel_write_safe": True}
