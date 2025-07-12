from typing import Self, Iterable, Generic, Iterator
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


def _delegate_comparison(rlist_method):
    """
    Wrap a comparison method with this decorator to delegate the method call to the underlying
    builtin list data structure of the rlist.
    When the argument is an rlist the underlying lists are compared.
    """

    @wraps(rlist_method)
    def call_list_method(self, other):
        if not isinstance(other, rlist):
            return getattr(self._list, rlist_method.__name__)(other)

        return getattr(self._list, rlist_method.__name__)(other._list)

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
        """
        Apply the given function to the items of the list and return a new instance
        of rlist with the mapped items.

        ## Example

        ```python
        from rlist import rlist
        from dataclasses import dataclass

        @dataclass
        class Person:
            id: int
            name: str

        people = rlist([Person(1, "John"), Person(2, "George"), Person(3, "Mike")])
        names = people.map(lambda p: p.name)
        ```
        """
        return rlist(map(func, self._list))

    @_delegate
    def pop(self, index=None) -> R: ...

    def reject(self, func: FilterFunc) -> Self:
        """
        Reject items from the list by applying the given function and return
        a new instance of rlist with the non-rejected items.

        ## Example

        ```python
        from rlist import rlist
        from dataclasses import dataclass

        @dataclass
        class Person:
            id: int
            name: str

        people = rlist([Person(1, "John"), Person(2, "George"), Person(3, "Mike")])
        people_without_e = people.reject(lambda p: 'e' in p.name)
        ```
        """
        return rlist(filterfalse(func, self._list))

    @_delegate
    def remove(self, item: R) -> R: ...

    @_delegate
    def reverse(self) -> None: ...

    def select(self, func: FilterFunc) -> Self:
        """
        Select items from the list by applying the given function and return
        a new instance of rlist with the selected items.

        ## Example

        ```python
        from rlist import rlist
        from dataclasses import dataclass

        @dataclass
        class Person:
            id: int
            name: str

        people = rlist([Person(1, "John"), Person(2, "George"), Person(3, "Mike")])
        people_with_e = people.select(lambda p: 'e' in p.name)
        ```
        """
        return rlist(filter(func, self._list))

    @_delegate
    def sort(self, *, key: SortFunc, reverse: bool = False) -> None: ...

    def __add__(self, other) -> Self:
        return rlist(self._list + other)

    @_delegate
    def __contains__(self, item: R) -> bool: ...

    @_delegate
    def __delitem__(self, item: R) -> None: ...

    @_delegate_comparison
    def __eq__(self, other) -> bool: ...

    @_delegate_comparison
    def __ge__(self, other) -> bool: ...

    @_delegate
    def __getitem__(self, index: int) -> R: ...

    @_delegate_comparison
    def __gt__(self, other) -> bool: ...

    @_delegate
    def __iter__(self) -> Iterator[R]: ...

    @_delegate_comparison
    def __le__(self, other) -> bool: ...

    @_delegate
    def __len__(self) -> int: ...

    @_delegate_comparison
    def __lt__(self, other) -> bool: ...

    def __mul__(self, other) -> Self:
        return rlist(self._list * other)

    @_delegate_comparison
    def __ne__(self, other) -> bool: ...

    def __repr__(self) -> str:
        return str(self)

    @_delegate
    def __reversed__(self) -> Iterator[R]: ...

    def __rmul__(self, other) -> Self:
        return rlist(other * self._list)

    @_delegate
    def __setitem__(self, index: int, item: R) -> None: ...

    @_delegate
    def __sizeof__(self) -> int: ...

    def __str__(self) -> str:
        return f"<rlist: {self._list}>"
