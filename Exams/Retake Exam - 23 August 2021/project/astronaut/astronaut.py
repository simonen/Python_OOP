from abc import ABC, abstractmethod
from typing import ClassVar


class Astronaut(ABC):
    _DECREASE_AMOUNT: int = 10

    def __init__(self, name: str, oxygen: int | None = None) -> None:
        self.name = name
        self.oxygen = oxygen if oxygen is not None else self._INITIAL_OXYGEN
        self.backpack: list[str] = []

    def breathe(self) -> None:
        self.oxygen = max(0, self.oxygen - self._DECREASE_AMOUNT)

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount

    @property
    @abstractmethod                # enforces subclasses to have the attribute.
    def _INITIAL_OXYGEN(self) -> int:
        ...

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value.split():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self._name = value

    def __str__(self) -> str:
        items = ", ".join(self.backpack) if self.backpack else "none"
        res = [f"Name: {self.name}", f"Oxygen: {self.oxygen}", f"Backpack items: {items}"]
        return '\n'.join(res)