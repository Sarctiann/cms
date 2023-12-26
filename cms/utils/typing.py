from typing import Callable, Literal, Optional, TypedDict

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
    forms: list[str]
    api_files: list[str]


ComponentMap = dict[str, Callable[..., rx.Component]]


class FormField(TypedDict):
    name: str
    type: Optional[str]
    label: Optional[str]
    placeholder: Optional[str]
    required: Optional[bool]
    handler: Optional[str]


class FormContent(TypedDict):
    fields: list[FormField]
