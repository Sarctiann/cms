import reflex as rx

__all__ = ["BaseState"]


class BaseState(rx.State):
    """
    A base state to split the App state into substates.
    Due only one state being allowed per component, this is a workaround.
    """

    pass
