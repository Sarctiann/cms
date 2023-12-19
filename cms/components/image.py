import reflex as rx

__all__ = ["image"]


def image(source) -> rx.Component:
    return rx.image(src=source, style=img_style)


img_style = dict(
    max_width="50vw",
    max_height="50vh",
)
