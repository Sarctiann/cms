import reflex as rx

from ..components import *
from ..pages.use_layout import use_layout
from ..state.pages_state import PagesState
from .content_file_error_page import content_file_error

__all__ = ["init_pages"]


def init_pages(app: rx.App) -> None:
    app.add_page(content_file_error, "/content_file_error")

    @rx.page("/[page_route]")
    @use_layout()
    def _() -> rx.Component:
        return rx.container(
            rx.markdown(
                PagesState.page_content,
                component_map=component_map,
            ),
            rx.box(style=box_style),
            style=container_style,
        )


container_style = dict(
    padding="1rem",
    max_width="90vw",
    max_height="100vh",
)

box_style = dict(
    height="10vh",
)
