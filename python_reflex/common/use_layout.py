from functools import wraps
import reflex as rx

__all__ = ["use_layout"]


def use_layout(children):
    @wraps(children)
    def with_layout(*args, **kwargs) -> rx.Component:
        return rx.box(
            rx.heading("(test layout)", size="sm"),
            children(*args, **kwargs),
            border_width="0.1em",
            border_radius="0.5em",
            padding="1em",
            border_color="red",
        )

    return with_layout
