from typing import Any

import reflex as rx

from cms.state.forms_state import FormsBaseState

__all__ = ["FormsHandlerState"]


class FormsHandlerState(FormsBaseState):
    """
    Here implement the handlers and of the forms and other vars
    """

    variables: dict[str, Any] = dict(
        # Declare your variables here
        #
        greeting="Hello default variable!",
    )

    # Declare your handlers here
    #
    def hello(self, data: dict) -> None:
        print(f"Hello {data['name']}!")
        self.variables["greeting"] = f"Hello {data['name']}!"
