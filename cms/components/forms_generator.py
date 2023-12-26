from typing import cast

import reflex as rx

from content.handler import FormsHandlerState


def jsonform(children: str, *args, **kwargs) -> rx.Component:
    return cast(
        rx.Component,
        rx.fragment(
            rx.cond(
                FormsHandlerState.declared_forms[children],
                rx.fragment(
                    generate_forn(children),
                    *args,
                    **kwargs,
                ),
                rx.text(
                    f' "{children}" form does not exist',
                    as_="span",
                    style=error_style,
                    *args,
                    **kwargs,
                ),
            ),
        ),
    )


error_style = dict(
    color="red",
)


def generate_forn(form_name: str) -> rx.Component:
    fields = FormsHandlerState.formfields[form_name]

    return rx.fragment(
        "Here goes the magic", rx.foreach(fields, lambda field: rx.text(field["name"]))
    )
