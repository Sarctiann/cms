from typing import Callable

import reflex as rx

from .index import *

__all__ = ["get_pages"]


def get_pages() -> list[Callable[[], rx.Component]]:
    return [
        index,
    ]
