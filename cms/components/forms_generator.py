from typing import cast

import reflex as rx
from cms.utils.typing import FormField

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
    return rx.form(
        rx.vstack(
            rx.foreach(
                FormsHandlerState.formfields[form_name],
                lambda field: generate_field(field),
            ),
            style=format_stack_style,
        )
    )


format_stack_style = dict(
    width="fit-content",
)


def generate_field(field: FormField) -> rx.Component:
    return rx.box(
        rx.cond(
            field.type == "text",
            rx.input(
                name=field.name,
                placeholder=field.placeholder,
            ),
        )
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
