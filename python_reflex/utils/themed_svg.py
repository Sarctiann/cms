import reflex as rx

__all__ = ["themed_svg"]


def themed_svg(img_name: str, colors: dict[str, tuple[str, str]]) -> rx.Component:
    """
        This utility changes the color of the given svg depending on the color_mode.
        In order to do that, you have to change the values of the `fill` attributes
        to an identifier suach as "color1" witch must match to the passed key argument.

    Parameters:
        * img_name: The name of the svg file (must be placed in assets).
        * colors: A variable amount of color pairs in order: light, dark
            (name must match the name given to the `fill` attribute)

    Returns:
        rx.Component: a logo svg.
    """
    for c in colors.values():
        assert len(c) % 2 == 0, ValueError("The length of the colors must be even.")

    with open(f"assets/{img_name}.svg", "r") as svg:
        svg_logo = svg.read()

    def replace_colors(str_svg: str, order: int):
        for c_id, color in colors.items():
            str_svg = str_svg.replace(c_id, color[order])

        return str_svg

    return rx.html(
        rx.color_mode_cond(replace_colors(svg_logo, 0), replace_colors(svg_logo, 1))
    )
