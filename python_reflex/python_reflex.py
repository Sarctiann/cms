"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from python_reflex.pages import index


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()


def algo(n):
    return n
