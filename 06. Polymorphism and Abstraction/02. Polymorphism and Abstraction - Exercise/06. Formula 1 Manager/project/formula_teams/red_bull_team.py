from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def expenses(self) -> int:
        return 250_000

    @staticmethod
    def sponsors() -> dict:
        sponsors = {
            'oracle': {1: 1_500_000, 2: 800_000},
            'honda': {8: 20_000, 10: 10_000}
        }

        return sponsors

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        earnings = self.sponsor_earnings(race_pos, self.sponsors())
        profit = earnings - self.expenses
        self.budget += profit

        return f"The revenue after the race is {profit}$. Current budget {self.budget}$"
