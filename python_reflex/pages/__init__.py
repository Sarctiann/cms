import reflex as rx

from .page_builder import *

__all__ = ["init_pages"]


def init_pages(app: rx.App) -> None:
    for page in get_pages():
        app.add_page(page)
