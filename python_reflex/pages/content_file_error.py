from ctypes import alignment
import reflex as rx

__all__ = ["content_file_error"]


def content_file_error() -> rx.Component:
    return rx.vstack(
        rx.heading(
            'Something went wrong traying to load the "_content.json" file',
            color="#DF1010",
            size="md",
        ),
        rx.button(
            "Retry",
            on_click=lambda: rx.redirect("/"),
            bg_color="lightblue",
        ),
        justify_content="center",
        height="100vh",
    )
