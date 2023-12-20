from calendar import c
import reflex as rx

from content.handler import FormsHandlerState

__all__ = ["variable"]


def variable(children: str, *args, **kwargs) -> rx.Component:
    child = FormsHandlerState.variables[children]
    return rx.fragment(
        child & child
        | rx.text(
            f' "{children}" var does not exist',
            style=error_style,
        ),
        *args,
        **kwargs,
    )


error_style = dict(
    color="red",
)
