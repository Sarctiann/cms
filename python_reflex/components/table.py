import reflex as rx

from ..utils.typing import ComponentMap

table: ComponentMap = dict(
    table=lambda *args, **kwargs: rx.table(*args, style=table_style, **kwargs),
    th=lambda *args, **kwargs: rx.th(*args, style=th_style, **kwargs),
    td=lambda *args, **kwargs: rx.td(*args, style=td_style, **kwargs),
)


table_style = dict(max_width="70vw")
th_style = dict()
td_style = dict()
