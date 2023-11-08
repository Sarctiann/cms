import reflex as rx

__all__ = ["about"]


def about() -> rx.Component:
    return rx.fragment(rx.heading("This is the about page."))
