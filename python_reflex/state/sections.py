from typing import TypedDict
import reflex as rx

from python_reflex.utils.get_file_content import file_to_json

from ._base_state import BaseState

__all__ = ["SectionState"]


class Section(TypedDict):
    page_title: str
    tab_label: str
    markdown_file_en: str
    markdown_file_es: str


class SectionState(BaseState):
    """The sections state."""

    sections: list[Section]

    @rx.var
    def tab_labels(self) -> list[str]:
        return [s["tab_label"] for s in self.sections]

    def _add_sections(self, sections_dict: dict) -> None:
        """Add sections to the state."""
        new_sections: list[Section] = [
            Section(
                page_title=s.get("page_title", ""),
                tab_label=s.get("tab_label", ""),
                markdown_file_en=s.get("markdown_file_en", ""),
                markdown_file_es=s.get("markdown_file_es", ""),
            )
            for s in sections_dict
            if all(attr in s for attr in s.keys())
        ]
        if self.sections == new_sections:
            print("...No secttion changes found")
        else:
            self.sections = new_sections

    def reload_sections(self) -> None:
        """Reload the sections."""
        self._add_sections(file_to_json("content/_sections.json"))

    def on_mount(self) -> None:
        """Load Sections the first time"""
        if len(self.sections) == 0:
            # print("...loading sections")
            self.reload_sections()
