import reflex as rx

from ..common import use_layout

__all__ = ["index"]


@use_layout()
def index() -> rx.Component:
    return rx.fragment(
        rx.heading(
            "My hardcoded index page",
            style=header_style,
        ),
        rx.markdown(
            """
            ### TODO:

            - test markdown
            - create components to render markdown
            - write a home_en and a home_es page
            """
        ),
    )


header_style = dict(font_size="4em", margin_top="1em")
