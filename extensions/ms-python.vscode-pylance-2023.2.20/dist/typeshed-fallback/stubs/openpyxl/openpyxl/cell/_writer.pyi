from _typeshed import Incomplete

def etree_write_cell(xf, worksheet, cell, styled: Incomplete | None = ...) -> None: ...
def lxml_write_cell(xf, worksheet, cell, styled: bool = ...) -> None: ...

write_cell = lxml_write_cell
write_cell = etree_write_cell
