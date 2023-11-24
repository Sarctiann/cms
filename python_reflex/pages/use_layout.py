from functools import wraps
from typing import Literal, cast

import reflex as rx

from ..state import AppBarState, PagesState

__all__ = ["use_layout"]


def use_layout():
    """Wraps a page with the layout.

    Args:
        TODO: add args to `use_layout` if it is needed.
    """

    def get_children(children):
        @wraps(children)
        def with_layout(*args, **kwargs) -> rx.Component:
            return rx.vstack(
                rx.hstack(
                    rx.html(
                        rx.color_mode_cond(
                            AppBarState.themed_svg_light,
                            AppBarState.themed_svg_dark,
                        )
                    ),
                    rx.spacer(),
                    rx.foreach(
                        PagesState.page_tabs,
                        lambda page: rx.fragment(
                            rx.button(
                                page[0],
                                on_click=rx.redirect(page[1]),
                                variant=tab_variant(page[2]),
                                color_scheme=tab_color_scheme(page[2]),
                                style=tab_style,
                            ),
                            rx.divider(orientation="vertical"),
                        ),
                    ),
                    rx.button(
                        rx.icon(tag="repeat"),
                        AppBarState.language,
                        on_click=AppBarState.toggle_language,
                        style=lang_btn,
                    ),
                    rx.color_mode_button(rx.color_mode_icon()),
                    id="nav_bar",
                    style=nav_bar_style,
                ),
                rx.vstack(
                    children(*args, **kwargs),
                    id="content",
                    style=content_style,
                ),
                id="layout_container",
                style=container_style,
            )

        return with_layout

    return get_children


container_style = dict(
    height="100vh",
    padding_bottom="0.1em",
    box_shadow=rx.color_mode_cond(
        "inset 0 -0.3em 0.5em 0 #377DB642",
        "inset 0 -0.3em 0.5em 0 #63589942",
    ),
)

nav_bar_style = dict(
    position="relative",
    z_index=2,
    width="100%",
    padding_block="0.5em",
    padding_inline="4em",
    box_shadow=rx.color_mode_cond(
        "0 0.3em 0.5em 0 #377DB642",
        "0 0.3em 0.5em 0 #63589942",
    ),
)


tab_style = dict(
    font_size="16px",
    font_weight="bold",
    min_width="max-content",
)


def tab_color_scheme(selected):
    return cast(
        Literal["telegram"] | None,
        rx.cond(selected == "True", "telegram", ""),
    )


def tab_variant(selected):
    return cast(
        Literal["ghost", "outline"],
        rx.cond(
            selected == "True",
            "outline",
            "ghost",
        ),
    )


lang_btn = dict(
    display="flex",
    gap="5px",
    text_transform="uppercase",
    min_width="5em",
)

content_style = dict(
    margin_top="0em !important",
    width="100%",
    overflow="auto",
)
