from calendar import c
from typing import cast
import reflex as rx

from content.handler import FormsHandlerState

__all__ = ["variable"]


def variable(children: str, *args, **kwargs) -> rx.Component:
    child = FormsHandlerState.variables[children]
    component = rx.cond(
        child,
        rx.fragment(
            child,
            *args,
            **kwargs,
        ),
        rx.text(
            f' "{children}" var does not exist',
            as_="span",
            style=error_style,
            *args,
            **kwargs,
        ),
    )
    return cast(rx.Component, component)


error_style = dict(
    color="red",
)
