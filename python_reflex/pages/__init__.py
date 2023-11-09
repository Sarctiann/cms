import reflex as rx

from .about import *
from .index import *

__all__ = ["init_pages"]


def init_pages(app: rx.App):
    app.add_page(index)
    app.add_page(about)
