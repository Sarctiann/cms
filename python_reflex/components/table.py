import reflex as rx

from ..utils.typing import ComponentMap

table: ComponentMap = dict(
    table=lambda *args, **kwargs: rx.table(*args, style=table_style, **kwargs),
    th=lambda *args, **kwargs: rx.th(*args, style=th_style, **kwargs),
    td=lambda *args, **kwargs: rx.td(*args, style=td_style, **kwargs),
)


table_style = dict(
    max_width="50vw",
    border="1px solid grey",
    border_collapse="separate",
    border_radius="0.7em 0.7em 0.2em 0.2em",
)
th_style = dict(
    font_size="1em",
)
td_style = dict()
