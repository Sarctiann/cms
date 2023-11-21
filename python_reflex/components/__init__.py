import reflex as rx

from ..utils.typing import ComponentMap
from .table import table
from .divider import divider
from .image import image

__all__ = ["component_map"]


component_map: ComponentMap = dict(**table, hr=divider, br=divider, img=image)
