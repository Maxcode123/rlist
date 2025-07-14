from unittest_extensions import TestCase, args
from dataclasses import dataclass

from rlist import rlist


@dataclass
class Model:
    name: str
    age: int
    attrs: dict | None = None


class TestRlistMap(TestCase):
    def models(self):
        return [
            Model(name="Johnny", age=28),
            Model(name="Yuri", age=41, attrs={"key": 1}),
            Model(name="Alexander", age=12),
            Model(name="Salomon", age=23),
        ]

    def _rlist(self, iterable):
        if iterable is None:
            return rlist(self.models())

        return rlist(iterable)

    def subject(self, func, iterable=None):
        return self._rlist(iterable).map(func)

    @args(func=lambda m: m)
    def test_simple_func(self):
        self.assertResult(self.models())

    @args(func=lambda m: m.name)
    def test_map_names(self):
        self.assertResult(["Johnny", "Yuri", "Alexander", "Salomon"])
