import reflex as rx

from ..utils.types import Section, Content
from ._base_state import BaseState

__all__ = ["SectionState"]


class SectionState(BaseState):
    """The sections state."""

    @rx.var
    def sections(self) -> list[Section] | None:
        if self.content:
            new_sections: list[Section] = [
                Section(
                    tab_label=s.get("tab_label", ""),
                    page_route=s.get("page_route", ""),
                    markdown_file_en=s.get("markdown_file_en", ""),
                    markdown_file_es=s.get("markdown_file_es", ""),
                )
                for s in self.content.get("sections")
                if all(attr in s for attr in s.keys())
            ]
            return new_sections

    @rx.var
    def tab_labels(self) -> list[str]:
        return [s["tab_label"] for s in self.sections or []]
