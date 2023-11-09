import reflex as rx

__all__ = ["devlights_iso"]


with open("assets/devlights_iso.svg", "r") as svg:
    svg_iso = svg.read()


def devlights_iso(color: str = "#8E408E") -> rx.Component:
    """This is the devlights isotipe logo.

    Args:
        color (str, optional): A valid css color.

    Returns:
        rx.Component: An svg logo.
    """
    return rx.html(svg_iso.replace("color", color))
