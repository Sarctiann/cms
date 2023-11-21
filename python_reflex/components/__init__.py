import reflex as rx

from ..utils.typing import ComponentMap
from .table import table

__all__ = ["component_map"]


component_map: ComponentMap = dict(
    **table,
)
