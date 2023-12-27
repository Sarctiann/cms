from typing import cast

import reflex as rx
from cms.utils.typing import FormField

from content.handler import FormsHandlerState


class FormsHandlerPostState(FormsHandlerState):
    """
    The purpose of this class is to keep clean the FormsHandlerState class
    """

    def call_handler(self, data: dict = {}) -> None:
        getattr(self, data["handler"])(data)


def jsonform(children: str, *args, **kwargs) -> rx.Component:
    cond = FormsHandlerPostState.declared_forms[children]
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
    handler = FormsHandlerPostState.form_handlers[form_name]
    return rx.form(
        rx.vstack(
            rx.foreach(
                FormsHandlerPostState.form_fields[form_name],
                lambda field: generate_field(field),
            ),
            # This input is used to call the handler
            rx.input(
                name="handler",
                type_="hidden",
                value=handler,
            ),
            style=format_stack_style,
        ),
        on_submit=FormsHandlerPostState.call_handler,
    )


format_stack_style = dict(
    width="fit-content",
    align_items="flex-start",
    min_height="max-content",
)


def generate_field(field: FormField) -> rx.Component:
    return rx.fragment(
        # TODO: refactor this when reflex supports rx.match
        rx.cond(
            field.type == "text",
            rx.fragment(
                rx.text(
                    field.label,
                    style=label_style,
                ),
                rx.input(
                    name=field.name,
                    placeholder=field.placeholder,
                    is_required=field.is_required,
                ),
            ),
        ),
        rx.cond(
            field.type == "submit",
            rx.button(
                field.label,
                name=field.name,
                style=button_style,
                type_="submit",
            ),
        ),
    )


label_style = dict(
    padding_left="16px",
)

button_style = dict(
    width="100%",
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
                    f"(create it in content/forms/{children}_{FormsHandlerPostState.language}.json)",
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
