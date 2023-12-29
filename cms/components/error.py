import reflex as rx

__all__ = ["error"]


def error(children, *args, **kwargs) -> rx.Component:
    return rx.fragment(
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
    )


error_style = dict(
    color="red",
    display="block",
)
