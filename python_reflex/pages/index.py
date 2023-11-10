import reflex as rx

from python_reflex.state.sections import SectionState

from ..common import use_layout

__all__ = ["index"]


@use_layout()
def index() -> rx.Component:
    return rx.fragment(
        rx.heading(
            "Devlights",
            style=header_style,
        ),
        rx.button("Reload Section", on_click=SectionState.reload_sections),
    )


header_style = dict(font_size="4em", margin_top="1em")
