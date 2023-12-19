from typing import Callable, Literal, TypedDict

import reflex as rx


class AppBarImg(TypedDict):
    svg_name: str
    colors: dict[str, tuple[str, str]]


class Page(TypedDict):
    page_title: str
    page_route: str
    md_file: str


class Content(TypedDict):
    app_bar_img: AppBarImg
    default_lang: Literal["en", "es"]
    pages: list[Page]


ComponentMap = dict[str, Callable[..., rx.Component]]
