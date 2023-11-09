"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from .api import init_api
from .pages import init_pages


# Add state and page to the app.
app = rx.App()

init_pages(app)
init_api(app)

app.compile()
