import reflex as rx

from ..common import use_layout

__all__ = ["index"]


@use_layout()
def index() -> rx.Component:
    return rx.fragment(
        rx.heading(
            "Devlights",
            style=header_style,
        ),
    )


header_style = dict(font_size="4em", margin_top="1em")
