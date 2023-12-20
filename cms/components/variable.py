import reflex as rx

from content.handler import FormsHandlerState

__all__ = ["variable"]


def variable(children: str, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        FormsHandlerState.variables[children],
        *args,
        **kwargs,
    )
