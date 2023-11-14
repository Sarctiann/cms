import reflex as rx

from python_reflex.utils.themed_svg import themed_svg

from ..utils.types import AppBarImg
from ._base_state import BaseState

__all__ = ["AppState"]


class AppState(BaseState):
    # @rx.var
    # def app_bar_img(self) -> AppBarImg | None:
    #     if self.content:
    #         abi = self.content.get("app_bar_img")
    #         return AppBarImg(
    #             svg_name=abi.get("svg_name"),
    #             colors={
    #                 c_id: (values[0], values[1])
    #                 for c_id, values in abi.get("colors").items()
    #             },
    #         )

    # @rx.var
    # def abi_name(self) -> str:
    #     return self.app_bar_img.get("svg_name")

    # @rx.var
    # def abi_colors(self) -> dict[str, tuple[str, str]]:
    #     return self.app_bar_img.get("colors")

    @rx.var
    def app_bar_img(self) -> rx.Component:
        abi = self.content.get("app_bar_img")
        return themed_svg(abi.get("svg_name"), abi.get("colors"))
