from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    _VALID_HORSES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    def _find_jockey(self, jockey_name: str):
        return next((x for x in self.jockeys if x.name == jockey_name), None)

    def _find_race(self, race_type: str) -> HorseRace | None:
        return next((x for x in self.horse_races if x.race_type == race_type), None)

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> str | None:
        if horse_type not in self._VALID_HORSES:
            return None

        if any(x for x in self.horses if x.name == horse_name):
            raise Exception("Horse {horse_name} has been already added!")

        horse = self._VALID_HORSES[horse_type](horse_name, horse_speed)
        self.horses.append(horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        if self._find_jockey(jockey_name) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self._find_race(race_type) is not None:
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_jockey(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horse_type not in self._VALID_HORSES:
            raise Exception("Horse breed {horse_type} could not be found!")

        horse = next((x for x in reversed(self.horses) if isinstance(x, self._VALID_HORSES[horse_type]) and not x.is_taken), None)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:
        race = self._find_race(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self._find_jockey(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._find_race(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey = max(race.jockeys, key=lambda x: x.horse.speed)

        return f"The winner of the {race_type} race, with a speed of {winner_jockey.horse.speed}km/h is {winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}."