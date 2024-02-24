from abc import abstractmethod, ABC


class FormulaTeam(ABC):

    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass

    @staticmethod
    def sponsor_earnings(race_pos: int, sponsors: dict) -> int:
        earnings = 0
        for position in sponsors.values():
            for pos in position:
                if race_pos <= pos:
                    earnings += position[pos]
                    break

        return earnings
