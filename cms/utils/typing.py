from typing import Callable, Literal

import reflex as rx


class AppBarImg(rx.Base):
    svg_name: str
    colors: dict[str, tuple[str, str]]


class Page(rx.Base):
    page_title: str
    page_route: str
    md_file: str


class Content(rx.Base):
    app_bar_img: AppBarImg
    default_lang: Literal["en", "es"]
    pages: list[Page]
    forms: list[str]


ComponentMap = dict[str, Callable[..., rx.Component]]


class FormField(rx.Base):
    name: str
    type: str
    label: str
    placeholder: str
    required: bool
    handler: str


class FormContent(rx.Base):
    fields: list[FormField]
