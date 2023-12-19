from functools import wraps

import reflex as rx

__all__ = ["use_red_box"]


def use_red_box(children):
    @wraps(children)
    def with_layout(*args, **kwargs) -> rx.Component:
        return rx.box(
            children(*args, **kwargs),
            outline="red solid 2px",
            outline_offset="-1px",
            bg="#ff101007",
        )

    return with_layout
