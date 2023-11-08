from functools import wraps
import reflex as rx

__all__ = ["use_layout"]


def use_layout(sections=[]):
    """Wraps a page with the layout.

    Args:
        sections (list, optional): A list of Tabs for the sections. Defaults to [].
    """

    def get_children(children):
        @wraps(children)
        def with_layout(*args, **kwargs) -> rx.Component:
            return rx.vstack(
                rx.hstack(
                    rx.spacer(),
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
    padding_inline="3em",
    box_shadow=rx.color_mode_cond(
        "0 0.3em 0.5em 0 #377DB642",
        "0 0.3em 0.5em 0 #63589942",
    ),
)

content_style = dict(
    margin_top="0em !important",
    width="100%",
    overflow="auto",
)
