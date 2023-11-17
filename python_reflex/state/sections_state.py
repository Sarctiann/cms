import reflex as rx

from ..utils.typing import Section
from ._base_state import BaseState

__all__ = ["SectionsState"]


class SectionsState(BaseState):
    """The sections state."""

    @rx.var
    def sections(self) -> list[Section] | None:
        if self.content:
            new_sections: list[Section] = [
                Section(
                    page_title=s.get("page_title", ""),
                    page_route=s.get("page_route", ""),
                    md_file_en=s.get("md_file_en", ""),
                    md_file_es=s.get("md_file_es", ""),
                )
                for s in self.content.get("sections")
                if all(attr in s for attr in s.keys())
            ]
            return new_sections

    @rx.var
    def page_titles(self) -> list[str]:
        return [s["page_title"] for s in self.sections or []]
