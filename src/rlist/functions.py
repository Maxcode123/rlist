from rlist.rlist import rlist
from rlist.types import FilterFunc, MapFunc


def selected(iterable: rlist, *, key: FilterFunc, reverse: bool = False) -> rlist: ...


def rejected(iterable: rlist, *, key: FilterFunc, reverse: bool = False) -> rlist: ...


def mapped(iterable: rlist, *, key: MapFunc, reverse: bool = False) -> rlist: ...
