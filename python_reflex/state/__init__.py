import reflex as rx

from ._base_state import BaseState
from .app import *
from .sections import *


def __init_state() -> rx.Component:
    return rx.fragment(on_mount=BaseState.on_mount)


def init_state(app: rx.App) -> None:
    app.add_page(__init_state, "/")
    pass
