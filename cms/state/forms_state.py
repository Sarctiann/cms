from typing import cast
from cms.utils.get_file_content import file_to_json
from ..utils.typing import FormContent, FormField
from ._base_state import BaseState

import reflex as rx

__all__ = ["FormsBaseState"]


class FormsBaseState(BaseState):
    @rx.var
    def jsonforms(self) -> dict[str, FormContent]:
        return {
            form_name: self.form_content(form_name)
            for form_name in self.content.get("forms", [])
        }

    @rx.var
    def declared_forms(self) -> dict[str, str]:
        return {k: k for k, _ in self.jsonforms.items()}

    @rx.var
    def formfields(self) -> dict[str, list[FormField]]:
        return {
            form_name: form_content["fields"]
            for form_name, form_content in self.jsonforms.items()
        }

    def form_content(self, form_name: str) -> FormContent:
        return cast(
            FormContent,
            file_to_json(
                f"content/forms/{form_name}_{self.language}.json",
            ),
        )
