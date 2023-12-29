from content.handler import FormsHandlerState


class PostFormsHandlerState(FormsHandlerState):
    """
    The purpose of this class is to keep clean the FormsHandlerState class
    """

    def call_handler(self, data: dict = {}) -> None:
        getattr(self, data["handler"])(data)
