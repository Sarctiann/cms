"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from .pages import *


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(about)
app.compile()
