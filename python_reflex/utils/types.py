from typing import TypedDict


class AppBarImg(TypedDict):
    svg_name: str
    colors: dict[str, tuple[str, str]]


class Section(TypedDict):
    tab_label: str
    page_route: str
    markdown_file_en: str
    markdown_file_es: str


class Content(TypedDict):
    app_bar_img: AppBarImg
    sections: list[Section]
