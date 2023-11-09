import reflex as rx

__all__ = ["devlights_logo"]


with open("assets/devlights_logo.svg", "r") as svg:
    svg_logo = svg.read()


def devlights_logo() -> rx.Component:
    """This variant of the devlights logo, changes color depending on the color_mode.

    Returns:
        rx.Component: An svg logo.
    """
    return rx.html(
        rx.color_mode_cond(
            svg_logo.replace("color", "#1E1F1D"), svg_logo.replace("color", "#FEFFFD")
        )
    )
