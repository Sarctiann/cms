import reflex as rx

__all__ = ["codeblock"]


def codeblock(*children, **props) -> rx.Component:
    return rx.code_block(*children, theme="dark", **props)
