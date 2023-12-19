import reflex as rx

from ..state._base_state import BaseState

__all__ = ["FormHandlerState"]


# Here implement the handlers of the forms
class FormHandlerState(BaseState):
    def hello(self, data: dict) -> None:
        print(f"Hello {data['name']}!")

    greeting = "HOLAAAA"
