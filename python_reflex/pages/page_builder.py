from typing import Callable

import reflex as rx

from .index import *
from .content_file_error import *

__all__ = ["get_pages"]


def get_pages() -> list[tuple[Callable[[], rx.Component], str | None]]:
    return [(content_file_error, "content_file_error"), (index, "home")]
