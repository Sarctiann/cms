import reflex as rx

__all__ = ["codeblock_light", "codeblock_dark"]


def codeblock_light(*children, **props) -> rx.Component:
    return rx.code_block(*children, theme="light", **props)


def codeblock_dark(*children, **props) -> rx.Component:
    return rx.code_block(*children, theme="dark", **props)
