from typing import List
from project.jockey import Jockey
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_specification.horse import Horse


class HorseRaceApp:

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> str or None:
        if any(h for h in self.horses if h.name == horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in ["Appaloosa", "Thoroughbred"]:
            new_horse = globals()[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str or None:
        if any(j for j in self.jockeys if j.name == jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str or None:
        if any(r for r in self.horse_races if r.race_type == race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> str or None:
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = next((h for h in self.horses[::-1] if h.__class__.__name__ == horse_type and not h.is_taken), None)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = next((hr for hr in self.horse_races if hr.race_type == race_type), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = next((hr for hr in self.horse_races if hr.race_type == race_type), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        jockeys = [j for j in horse_race.jockeys]
        winner = max(jockeys, key=lambda j: j.horse.speed)

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."
