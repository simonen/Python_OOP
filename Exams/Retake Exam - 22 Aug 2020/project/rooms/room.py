from typing import List
from project.people.child import Child
from project.appliances.appliance import Appliance


class Room:

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0

    def calculate_expenses(self, *args):
        for arg in args:
            if isinstance(arg[0], Appliance):
                self.expenses += sum(x.get_monthly_expense() for x in arg)
            if isinstance(arg[0], Child):
                self.expenses += sum(x.cost * 30 for x in arg)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value