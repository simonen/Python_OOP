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
    def room_cost(self):
        return self._ROOM_COST

    @property
    def current_expenses(self) -> float | int:
        return self.calculate_expenses(*self.children, *self.appliances)

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value: float) -> None:
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self._expenses = value

    def calculate_expenses(self, *args: Child | Appliance):
        return sum(x.get_monthly_expense() for x in args) + self.room_cost

    def count_residents(self) -> int:
        return self.members_count + len(self.children)
