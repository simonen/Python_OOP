from abc import ABC


class FormulaTeam(ABC):
    SPONSORS: dict[str, dict]
    EXPENSES: int
    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value: int):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = sum(self.collect_prize(prizes, race_pos) for prizes in self.SPONSORS.values()) - self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def collect_prize(prizes: dict, race_pos: int) -> int:
        qualifying_places = [place for place in prizes if race_pos <= place]
        if not qualifying_places:
            return 0
        return prizes[min(qualifying_places)]
