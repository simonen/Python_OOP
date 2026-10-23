from project.band_members.musician import Musician
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.concert import Concert
from project.band import Band


class ConcertTrackerApp:
    _VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def _find_band(self, band_name: str) -> Band | None:
        return next((x for x in self.bands if x.name == band_name), None)

    def _find_musician(self, musician_name: str) -> Musician | None:
        return next((x for x in self.musicians if x.name == musician_name), None)

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self._VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        if self._find_musician(name) is not None:
            raise Exception(f"{name} is already a musician!")

        musician = self._VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self._find_band(name) is not None:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if any(x for x in self.concerts if x.place == place):
            raise Exception(f"{place} is already registered for {genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician(musician_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self._find_band(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._find_band(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = self._find_musician(musician_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band(band_name)
        if band is None:
            return None

        if set(x.__class__.__name__ for x in band.members) != set(self._VALID_MUSICIANS):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next((x for x in self.concerts if x.place == concert_place))
        band_skills = [skill for member in band.members for skill in member.skills]

        if not set(concert.genres[concert.genre]).issubset(set(band_skills)):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
