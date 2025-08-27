from docutils import nodes
from docutils.parsers.rst import roles


def poly_icon_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom role for GeoGebra icons.
    Usage: {ggb-icon}`mode_intersect`

    This will generate a proper image node that Sphinx can process.
    """
    # Clean up the icon name (remove any extra whitespace)
    icon_name = text.strip()

    # Build the image path relative to the source directory
    img_src = f"/_static/icons/polyicons/{icon_name}.svg"

    # Create a proper image node that Sphinx can process
    node = nodes.image(uri=img_src, alt=f"Cubic {icon_name} icon")

    # Add the inline-image class
    node["classes"] = ["inline-image"]

    return [node], []


def setup(app):
    """Setup function to register the role with Sphinx."""
    # Register the role
    roles.register_local_role("poly-icon", poly_icon_role)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
