from unittest_extensions import TestCase, args
from dataclasses import dataclass

from rlist import rlist


@dataclass
class DataclassModel:
    name: str
    age: int
    attrs: dict | None = None


class TestRlist(TestCase):
    model_cls = DataclassModel

    def models(self):
        return [
            self.model_cls(name="Johnny", age=28),
            self.model_cls(name="Yuri", age=41, attrs={"key": 1}),
            self.model_cls(name="Alexander", age=12),
            self.model_cls(name="Salomon", age=23),
        ]

    def _rlist(self, iterable=None):
        if iterable is None:
            return rlist(self.models())

        return rlist(iterable)


class TestRlistMap(TestRlist):
    def subject(self, func, iterable=None):
        return self._rlist(iterable).map(func)

    @args(func=lambda m: m)
    def test_identity_func(self):
        self.assertResult(self.models())

    @args(func=lambda m: m.name)
    def test_map_names(self):
        self.assertResult(["Johnny", "Yuri", "Alexander", "Salomon"])

    def test_map_chains(self):
        result = self._rlist().map(lambda m: m.age).map(lambda a: a * 2)
        self.assertCountEqual([56, 82, 24, 46], result)

    def test_no_argument_raises(self):
        with self.assertRaises(TypeError):
            self._rlist().map()

    def test_identity_func_creates_new_list_object(self):
        lst = self._rlist()
        self.assertIsNot(lst, lst.map(lambda m: m))

    def test_identity_func_creates_shallow_copy(self):
        lst = self._rlist()
        obj = lst[0]
        copy_lst = lst.map(lambda m: m)
        self.assertIs(obj, copy_lst[0])

    @args(func=lambda m: m.name, iterable=[])
    def test_empty_list_accepts_func(self):
        self.assertResult([])

    @args(func="non-callable object")
    def test_non_callable_argument_raises(self):
        self.assertResultRaises(TypeError)

    @args(func=str, iterable=[1, 2, 3])
    def test_str_func(self):
        self.assertResult(["1", "2", "3"])


class TestRlistReject(TestRlist):
    def subject(self, func, iterable=None):
        return self._rlist(iterable).reject(func)

    @args(func=lambda m: True)
    def test_always_true(self):
        self.assertResult([])

    @args(func=lambda m: False)
    def test_always_false(self):
        self.assertResult(self.models())

    @args(func=lambda i: i > 2, iterable=[0, 1, 2, 3])
    def test_greater_than_func(self):
        self.assertResult([0, 1, 2])

    def test_creates_new_list_object(self):
        lst = rlist([1, 2, 3])
        new = lst.reject(lambda i: i == 2)
        self.assertIsNot(lst, new)

    def test_no_argument_raises(self):
        with self.assertRaises(TypeError):
            self._rlist().reject()

    def test_reject_chains(self):
        lst = rlist([1, 2, 3, 4, 5, 6]).reject(lambda i: i > 5).reject(lambda i: i == 2)
        self.assertCountEqual(lst, [1, 3, 4, 5])

    @args(func="non-callable object")
    def test_non_callable_argument_raises(self):
        self.assertResultRaises(TypeError)

    @args(func=lambda m: m.name, iterable=[])
    def test_empty_list_accepts_func(self):
        self.assertResult([])

    def test_always_false_func_creates_shallow_copy(self):
        lst = self._rlist()
        obj = lst[0]
        copy_lst = lst.reject(lambda m: False)
        self.assertIs(obj, copy_lst[0])

class TestRlistSelect(TestRlist):
    def subject(self, func, iterable=None):
        return self._rlist(iterable).select(func)

    @args(func=lambda m: True)
    def test_always_true(self):
        self.assertResult(self.models())

    @args(func=lambda m: False)
    def test_always_false(self):
        self.assertResult([])

    @args(func=lambda i: i > 2, iterable=[0, 1, 2, 3])
    def test_greater_than_func(self):
        self.assertResult([3])

    def test_creates_new_list_object(self):
        lst = rlist([1, 2, 3])
        new = lst.select(lambda i: i == 2)
        self.assertIsNot(lst, new)

    def test_no_argument_raises(self):
        with self.assertRaises(TypeError):
            self._rlist().select()

    def test_select_chains(self):
        lst = rlist([1, 2, 3, 4, 5, 6]).select(lambda i: i > 2).select(lambda i: i > 4)
        self.assertCountEqual(lst, [5, 6])

    @args(func="non-callable object")
    def test_non_callable_argument_raises(self):
        self.assertResultRaises(TypeError)

    @args(func=lambda m: m.name, iterable=[])
    def test_empty_list_accepts_func(self):
        self.assertResult([])

    def test_always_false_func_creates_shallow_copy(self):
        lst = self._rlist()
        obj = lst[0]
        copy_lst = lst.select(lambda m: True)
        self.assertIs(obj, copy_lst[0])
