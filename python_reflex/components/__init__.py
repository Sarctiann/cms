from ..utils.typing import ComponentMap
from .divider import divider
from .image import image
from .table import table

__all__ = ["component_map"]


component_map: ComponentMap = dict(
    **table,
    hr=divider,
    br=divider,
    img=image,
)
