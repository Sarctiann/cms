"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from .api import init_api
from .pages import init_pages
from .state import init_state

app = rx.App()

init_state(app)
init_pages(app)
init_api(app)

app.compile()
