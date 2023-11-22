import reflex as rx

from ..utils.get_file_content import file_to_str
from ..utils.typing import Page
from ._base_state import BaseState

__all__ = ["PagesState"]


class PagesState(BaseState):
    """The pages state."""

    @rx.var
    def pages(self) -> list[Page] | None:
        if self.content:
            new_pages: list[Page] = [
                Page(
                    page_title=s.get("page_title", ""),
                    page_route=s.get("page_route", ""),
                    md_file_en=s.get("md_file_en", ""),
                    md_file_es=s.get("md_file_es", ""),
                )
                for s in self.content.get("pages")
                if all(attr in s for attr in s.keys())
            ]
            return new_pages

    @rx.var
    def page_tabs(self) -> list[tuple[str, str, str]]:
        url = self.router.page.params.get("page_route", "")
        return [
            (s["page_title"], s["page_route"], str(s["page_route"] == url))
            for s in self.pages or []
        ]

    @rx.var
    def en_md_files(self) -> list[str]:
        return [s["md_file_en"] for s in self.pages or []]

    @rx.var
    def es_md_files(self) -> list[str]:
        return [s["md_file_es"] for s in self.pages or []]

    @rx.var
    def current_page_index(self) -> int | None:
        url = self.router.page.params.get("page_route", "")
        routes = [s["page_route"] for s in self.pages or []]
        if url not in routes:
            return None
        return routes.index(url)

    @rx.var
    def page_content(self) -> str:
        if (index := self.current_page_index) is None:
            return ""
        pages = self.en_md_files if self.language == "en" else self.es_md_files
        content = file_to_str(f"content/{pages[index]}")
        return content
