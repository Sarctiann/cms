from typing import cast

import reflex as rx

from content.handler import FormsHandlerState


def jsonform(children: str, *args, **kwargs) -> rx.Component:
    cond = FormsHandlerState.declared_forms[children]
    return cast(
        rx.Component,
        rx.cond(
            cond,
            rx.fragment(
                generate_form(children),
                *args,
                **kwargs,
            ),
            form_error(cond, children, *args, **kwargs),
        ),
    )


def generate_form(form_name: str) -> rx.Component:
    fields = FormsHandlerState.formfields[form_name]

    return rx.box(
        "Here goes the magic",
        rx.foreach(
            fields,
            lambda field: rx.text(field["name"]),
        ),
    )


def form_error(cond, children, *args, **kwargs) -> rx.Component:
    return cast(
        rx.Component,
        rx.cond(
            cond == False,
            rx.fragment(
                rx.text(
                    f' "{children}" form files does not exist',
                    as_="span",
                    style=missing_files_error_style,
                ),
                rx.text(
                    f"(create it in content/forms/{children}_{FormsHandlerState.language}.json)",
                    as_="span",
                    style=missing_files_error_style,
                ),
                *args,
                **kwargs,
            ),
            rx.fragment(
                rx.text(
                    f' "{children}" form is not declared',
                    as_="span",
                    style=missing_declaration_error_style,
                ),
                rx.text(
                    f'(declare it in content/_content.json: forms: [..., "{children}"])',
                    as_="span",
                    style=missing_declaration_error_style,
                ),
                *args,
                **kwargs,
            ),
        ),
    )


missing_files_error_style = dict(
    color="orangered",
    display="block",
)

missing_declaration_error_style = dict(
    color="red",
    display="block",
)
