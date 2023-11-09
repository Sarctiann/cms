import reflex as rx

__all__ = ["devlights_logo_mc"]


with open("assets/devlights_logo.svg", "r") as svg:
    svg_logo = svg.read()


def devlights_logo_mc(color: str = "#1E1F1D") -> rx.Component:
    """This is a monocromatic version of the devlights logo.

    Args:
        color (str, optional): A valid css color.

    Returns:
        rx.Component: An svg logo.
    """
    return rx.html(
        rx.color_mode_cond(
            svg_logo.replace("color", color), svg_logo.replace("color", color)
        )
    )
