from typing import Literal, TypedDict


class AppBarImg(TypedDict):
    svg_name: str
    colors: dict[str, tuple[str, str]]


class Section(TypedDict):
    page_title: str
    page_route: str
    md_file_en: str
    md_file_es: str


class Content(TypedDict):
    app_bar_img: AppBarImg
    default_lang: Literal["en", "es"]
    sections: list[Section]
