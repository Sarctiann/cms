from typing import cast

import reflex as rx

from ..utils import file_to_json
from ..utils.types import Content

__all__ = ["BaseState"]


class BaseState(rx.State):
    """
    A base state to split the App state into substates.
    Due only one state being allowed per component, this is a workaround.
    """

    @rx.var
    def content(self) -> Content | None:
        try:
            return cast(Content, file_to_json("content/_content.json"))
        except:
            print('Something went wrong traying to load the "_content.json" file')

    def on_mount(self) -> rx.event.EventSpec | None:
        """Reload the content state."""
        try:
            redirect = rx.redirect(self.content["sections"][0]["page_route"])
            print(f'redirecting to "{self.content["sections"][0]["page_route"]}"')
            return redirect

        except:
            print('Something went wrong traying to load the "_content.json" file')
            return rx.redirect("content_file_error")
