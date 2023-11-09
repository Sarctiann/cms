import json
from functools import wraps
import reflex as rx

from python_reflex.utils import devlights_logo

__all__ = ["use_layout"]


with open("content/_sections.json", "r") as f:
    pages = json.load(f)


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
                    devlights_logo(),
                    rx.spacer(),
                    rx.tabs(
                        rx.tab_list(
                            *[
                                rx.tab(
                                    section["tab_label"],
                                    style=tab_style,
                                )
                                for section in pages
                            ],
                        ),
                        variant="enclosed",
                    ),
                    rx.color_mode_button(rx.color_mode_icon(), float="right"),
                    id="nav_bar",
                    style=nav_bar_style,
                ),
                rx.vstack(children(*args, **kwargs), id="content", style=content_style),
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
    font_size="18px",
    font_weight="bold",
    min_width="max-content",
)

content_style = dict(
    margin_top="0em !important",
    width="100%",
    overflow="auto",
)
