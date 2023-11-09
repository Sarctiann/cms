import reflex as rx

from python_reflex.common import use_layout

__all__ = ["index"]


@use_layout()
def index() -> rx.Component:
    return rx.fragment(
        rx.heading("Devlights", font_size="4em", style=header_style),
    )


header_style = dict(margin_top="1em")
