from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:

    def __init__(self) -> None:
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int):
        valid_names = ["Red Bull", "Mercedes"]
        if team_name not in valid_names:
            raise ValueError("Invalid team name!")

        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        rb_revenue_msg = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        me_revenue_msg = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        leading_team = 'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'

        return f"Red Bull: {rb_revenue_msg}. Mercedes: {me_revenue_msg}." \
               f" {leading_team} is ahead at the {race_name} race."
