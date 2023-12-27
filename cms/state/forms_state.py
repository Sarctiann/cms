from typing import cast
from cms.utils.get_file_content import file_to_json
from ..utils.typing import FormContent, FormField
from ._base_state import BaseState

import reflex as rx

__all__ = ["FormsBaseState"]


class FormsBaseState(BaseState):
    @rx.var
    def jsonforms(self) -> dict[str, FormContent | None]:
        if self.content is None:
            return {}
        return {
            form_name: self.form_content(form_name) for form_name in self.content.forms
        }

    @rx.var
    def declared_forms(self) -> dict[str, bool]:
        return {
            form_name: (True if form_json_content is not None else False)
            for form_name, form_json_content in self.jsonforms.items()
        }

    @rx.var
    def formfields(self) -> dict[str, list[FormField]]:
        return {
            form_name: form_json_content["fields"]
            for form_name, form_json_content in self.jsonforms.items()
            if form_json_content is not None
        }

    def form_content(self, form_name: str) -> FormContent | None:
        try:
            content = cast(
                FormContent,
                file_to_json(
                    f"content/forms/{form_name}_{self.language}.json",
                ),
            )
        except FileNotFoundError:
            content = None

        return content
