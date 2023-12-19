import reflex as rx

from ..utils.typing import ComponentMap

table: ComponentMap = dict(
    table=lambda *children, **props: rx.table(*children, style=table_style, **props),
    thead=lambda *children, **props: rx.thead(*children, style=thead_style, **props),
    tbody=lambda *children, **props: rx.tbody(*children, style=tbody_style, **props),
    tr=lambda *children, **props: rx.tr(*children, **props),
    th=lambda *children, **props: rx.th(*children, style=th_style, **props),
    td=lambda *children, **props: rx.td(*children, style=td_style, **props),
)


table_style = dict(
    max_width="50vw",
    border="1px solid grey",
    border_collapse="separate",
    border_radius="0.7em 0.7em 0.2em 0.2em",
)

thead_style = dict()

tbody_style = dict()

tr_style = dict()

th_style = dict(
    font_size="1em",
)

td_style = dict()
