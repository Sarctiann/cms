import reflex as rx

from .index import *

__all__ = ["init_pages"]


def init_pages(app: rx.App):
    app.add_page(index)
