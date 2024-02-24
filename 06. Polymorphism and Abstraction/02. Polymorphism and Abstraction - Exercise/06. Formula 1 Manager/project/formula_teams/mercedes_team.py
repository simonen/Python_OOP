from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def expenses(self) -> int:
        return 200_000

    @staticmethod
    def sponsors() -> dict:
        sponsors = {
            'petronas': {1: 1_000_000, 3: 500_000},
            'teamviewer': {5: 100_000, 7: 50_000}
        }

        return sponsors

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        earnings = self.sponsor_earnings(race_pos, self.sponsors())
        profit = earnings - self.expenses
        self.budget += profit

        return f"The revenue after the race is {profit}$. Current budget {self.budget}$"
