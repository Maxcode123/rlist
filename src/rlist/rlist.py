from typing import Self, Iterable, Generic
from itertools import filterfalse
from functools import wraps
from sys import maxsize

from rlist.types import R, SortFunc, FilterFunc, MapFunc


def _delegate(rlist_method):
    """
    Wrap a method with this decorator to delegate the method call to the underlying
    builtin list data structure of the rlist.
    """
    @wraps(rlist_method)
    def call_list_method(self, *args, **kwargs):
        return getattr(self._list, rlist_method.__name__)(*args, **kwargs)

    return call_list_method


class rlist(Generic[R]):
    """
    Record list, provides handy methods for filtering items in addition to all the
    standard methods the built-in list provides.
    """

    def __init__(self, items: Iterable[R] = list()) -> None:
        self._list: list[R] = list(items)

    @_delegate
    def append(self, item: R) -> None: ...

    @_delegate
    def clear(self) -> None: ...

    def copy(self) -> Self:
        return rlist(self._list)

    @_delegate
    def count(self, item: R) -> int: ...

    @_delegate
    def extend(self, iterable: Iterable[R]) -> None: ...

    @_delegate
    def index(self, item: R, start: int = 0, stop: int = maxsize) -> int: ...

    @_delegate
    def insert(self, index: int, item: R) -> None: ...

    def map(self, func: MapFunc) -> Self:
        return rlist(map(func, self._list))

    @_delegate
    def pop(self, index=None) -> R: ...

    def reject(self, func: FilterFunc) -> Self:
        return rlist(filterfalse(func, self._list))

    @_delegate
    def remove(self, item: R) -> R: ...

    def reverse(self) -> Self: ...

    def select(self, func: FilterFunc) -> Self:
        return rlist(filter(func, self._list))

    @_delegate
    def sort(self, *, key: SortFunc, reverse: bool = False) -> None: ...

    @_delegate
    def __add__(self, other) -> Self: ...

    @_delegate
    def __contains__(self, item: R) -> bool: ...

    @_delegate
    def __delitem__(self, item: R) -> None: ...

    def __eq__(self, other) -> bool: ...

    def __ge__(self, other) -> bool: ...

    @_delegate
    def __getitem__(self, index: int) -> R: ...

    def __gt__(self, other) -> bool: ...

    @_delegate
    def __iter__(self) -> Iterable: ...

    def __le__(self, other) -> bool: ...

    @_delegate
    def __len__(self) -> int: ...

    def __lt__(self, other) -> bool: ...

    def __mul__(self, other) -> Self: ...

    def __ne__(self, other) -> bool: ...

    def __repr__(self) -> str: ...

    @_delegate
    def __reversed__(self) -> Self: ...

    def __rmul__(self, other) -> Self: ...

    @_delegate
    def __setitem__(self, index: int, item: R) -> None: ...

    @_delegate
    def __sizeof__(self) -> int: ...

    def __str__(self) -> str: ...
