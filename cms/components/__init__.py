from ..utils.typing import ComponentMap
from .codeblock import *
from .divider import *
from .image import *
from .table import *

import reflex as rx

__all__ = ["component_map_light", "component_map_dark"]


component_map: ComponentMap = dict(
    **table,
    hr=divider,
    br=divider,
    img=image,
)

component_map_light: ComponentMap = dict(
    **component_map,
    codeblock=codeblock_light,
)
component_map_dark: ComponentMap = dict(
    **component_map,
    codeblock=codeblock_dark,
)
