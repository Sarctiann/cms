from typing import Any

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
        markdown="## Markdown default variable!",
    )

    # Declare your handlers here
    #
    def hello(self, data: dict) -> None:
        print(f"Hello {data['name']}!")

        self.variables[
            "greeting"
        ] = f"## Hello {data['name']}! Your email is {data['email']}"

        self.variables[
            "markdown"
        ] = f"## Hello {data['name']}! Your email is {data['email']}"
