from typing import cast
import reflex as rx

from content.handler import FormsHandlerState

__all__ = ["variable"]


def variable(children: str, *args, **kwargs) -> rx.Component:
    child = FormsHandlerState.variables[children]
    return cast(
        rx.Component,
        rx.cond(
            child,
            rx.fragment(
                child,
                *args,
                **kwargs,
            ),
            rx.fragment(
                rx.text(
                    f' "{children}" var does not exist',
                    as_="span",
                    style=error_style,
                ),
                rx.text(
                    f'(declare it in content/handler.py: variables = dict(..., "{children}"="some value")',
                    as_="span",
                    style=error_style,
                ),
                *args,
                **kwargs,
            ),
        ),
    )


error_style = dict(
    color="red",
    display="block",
)
