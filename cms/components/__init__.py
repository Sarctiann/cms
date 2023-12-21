from ..utils.typing import ComponentMap
from .divider import *
from .image import *
from .table import *
from .variable import *

__all__ = ["component_map"]

component_map: ComponentMap = dict(
    **table,
    hr=divider,
    br=divider,
    img=image,
    variable=variable,
)
