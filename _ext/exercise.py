from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

logger = logging.getLogger(__name__)


class ExerciseDirective(SphinxDirective):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "level": directives.unchanged,
    }

    def run(self):
        title = self.arguments[0]
        # Create the admonition node
        admonition_node = nodes.admonition()

        admonition_node["classes"] = ["admonition", "exercise"]

        if self.options.get("level"):
            level = self.options.get("level")
            if level == "1":
                admonition_node["classes"] = ["admonition", f"common"]
            elif level == "2":
                admonition_node["classes"] = ["admonition", f"rare"]
            elif level == "3":
                admonition_node["classes"] = ["admonition", f"epic"]
            elif level == "4":
                admonition_node["classes"] = ["admonition", f"legendary"]
            else:
                admonition_node["classes"] = ["admonition", "exercise"]
        else:
            admonition_node["classes"] = ["admonition", "exercise"]

        # Create the title node
        title_node = nodes.title()
        parsed_title, _ = self.state.inline_text(title, self.lineno)
        title_node += parsed_title
        admonition_node += title_node

        # Parse the content
        self.state.nested_parse(self.content, self.content_offset, admonition_node)

        return [admonition_node]


def setup(app):
    app.add_directive("exercise", ExerciseDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
