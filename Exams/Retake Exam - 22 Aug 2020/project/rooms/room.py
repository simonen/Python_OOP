from typing import ClassVar
from project.people.child import Child
from project.appliances.appliance import Appliance


class Room:
    _ROOM_COST: ClassVar[float | int]

    def __init__(self, name: str, budget: float, members_count: int):
        self.name = name
        self.budget = budget
        self.members_count = members_count
        self.children: list[Child] = []
        self.appliances: list[Appliance] = []
        self.expenses = 0

    @property
    def room_cost(self) -> float | int:
        return self._ROOM_COST

    @property
    def current_expenses(self) -> float | int:
        return self.calculate_expenses(*self.children, *self.appliances)

    @property
    def expenses(self) -> float:
        return self._expenses

    @expenses.setter
    def expenses(self, value: float) -> None:
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self._expenses = value

    def calculate_expenses(self, *items: Child | Appliance) -> float:
        """Sum room cost plus monthly expenses of appliances and children (if any)"""
        return self.room_cost + sum(item.get_monthly_expense() for item in items)

    def count_residents(self) -> int:
        return self.members_count + len(self.children)
