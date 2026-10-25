from abc import ABC
from typing import ClassVar


class Appliance(ABC):
    _COST: ClassVar[float | int]
    _UNSET = object()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "_COST" not in cls.__dict__:  # note: __dict__, not hasattr
            raise TypeError(f"{cls.__name__} must define _COST")

    def __init__(self, cost: float = _UNSET) -> None:
        self.cost = self._COST if cost == self._UNSET else cost

    def get_monthly_expense(self):
        return self.cost * 30