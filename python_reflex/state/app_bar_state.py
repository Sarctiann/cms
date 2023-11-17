import reflex as rx

from ..utils.typing import Content
from ._base_state import BaseState

__all__ = ["AppBarState"]


class AppBarState(BaseState):
    @rx.var
    def themed_svg_light(self) -> str:
        logo_name, logo_colors = self.__get_name_and_colors(self.content)
        with open(f"assets/{logo_name}.svg", "r") as svg:
            svg_logo = svg.read()
            for c_id, color in logo_colors.items():
                svg_logo = svg_logo.replace(c_id, color[0])

        return svg_logo

    @rx.var
    def themed_svg_dark(self) -> str:
        logo_name, logo_colors = self.__get_name_and_colors(self.content)
        with open(f"assets/{logo_name}.svg", "r") as svg:
            svg_logo = svg.read()
            for c_id, color in logo_colors.items():
                svg_logo = svg_logo.replace(c_id, color[1])

        return svg_logo

    def toggle_language(self) -> None:
        self.language = "en" if self.language == "es" else "es"

    def __get_name_and_colors(
        self, cnt: Content
    ) -> tuple[str, dict[str, tuple[str, str]]]:
        logo = cnt.get("app_bar_img")
        name = logo.get("svg_name")
        colors = logo.get("colors")
        for c in colors.values():
            assert len(c) % 2 == 0, ValueError("The length of the colors must be even.")
        return (name, colors)
