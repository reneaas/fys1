from docutils import nodes
from docutils.parsers.rst import Directive, directives


class DialogueWrapperNode(nodes.General, nodes.Element):
    pass


class DialogueEntryNode(nodes.Admonition, nodes.Element):
    pass


def visit_dialogue_wrapper_node_html(self, node):
    self.body.append('<div class="dialogue">')


def depart_dialogue_wrapper_node_html(self, node):
    self.body.append("</div>")


def visit_dialogue_entry_node_html(self, node):
    self.body.append(f'<div class="dialogue-entry {node["css_class"]}">')
    self.body.append(f'<div class="speaker-name">{node["speaker_name"]}</div>')


def depart_dialogue_entry_node_html(self, node):
    self.body.append("</div>")


class DialogueDirective(Directive):
    has_content = True
    required_arguments = 0
    option_spec = {
        "name1": directives.unchanged_required,
        "name2": directives.unchanged_required,
        "speaker1": lambda s: directives.choice(s, ("left", "right")),
        "speaker2": lambda s: directives.choice(s, ("left", "right")),
    }

    def run(self):
        name1 = self.options.get("name1")
        name2 = self.options.get("name2")
        class1 = "speaker1" if self.options.get("speaker1") == "left" else "speaker2"
        class2 = "speaker1" if self.options.get("speaker2") == "left" else "speaker2"

        wrapper_node = DialogueWrapperNode()
        for line in self.content:
            line = line.strip()
            if not line or ":" not in line:
                continue

            speaker_name, message = line.split(":", 1)
            speaker_name = speaker_name.strip()
            message = message.strip()

            if speaker_name == name1:
                css_class = class1
            elif speaker_name == name2:
                css_class = class2
            else:
                continue

            entry_node = DialogueEntryNode()
            entry_node["css_class"] = css_class
            entry_node["speaker_name"] = speaker_name

            # Parse the message line like normal content so math works
            self.state.nested_parse([message], self.content_offset, entry_node)
            wrapper_node += entry_node

        return [wrapper_node]


def setup(app):
    app.add_node(
        DialogueWrapperNode,
        html=(visit_dialogue_wrapper_node_html, depart_dialogue_wrapper_node_html),
    )
    app.add_node(
        DialogueEntryNode,
        html=(visit_dialogue_entry_node_html, depart_dialogue_entry_node_html),
    )
    app.add_directive("dialogue", DialogueDirective)
    return {"version": "0.4"}
