from docutils import nodes
from docutils.parsers.rst import Directive


class ClearDirective(Directive):
    has_content = False

    def run(self):
        return [nodes.raw("", '<div style="clear: both;"></div>', format="html")]


def setup(app):
    app.add_directive("clear", ClearDirective)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
