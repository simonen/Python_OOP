from typing import List
from project.band_members.musician import Musician
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Drummer, Guitarist, Singer] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")

        if any(m for m in self.musicians if m.name == name):
            raise Exception(f"{name} is already a musician!")

        new_musician = globals()[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        if any(b for b in self.bands if b.name == name):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        current_concert = next((c for c in self.concerts if c.place == place), None)
        if current_concert:
            concert_genre = current_concert.genre
            raise Exception(f"{place} is already registered for {concert_genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.valid_band(band_name)
        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str or None:
        band = self.valid_band(band_name)
        musician = next((m for m in band.members if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str or None:
        band = next(b for b in self.bands if b.name == band_name)
        musician_types = [m for m in list(map(lambda x: x.__class__.__name__, band.members))]
        concert = next(c for c in self.concerts if c.place == concert_place)

        req = ["Guitarist", "Drummer", "Singer"]
        if set(req) != set(musician_types):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        band_skills_nested = [m.skills for m in band.members]
        band_skills = [skill for sublist in band_skills_nested for skill in sublist]

        if not set(Concert.concertz[concert.genre]).issubset(set(band_skills)):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        return f"{band_name} gained {((concert.audience * concert.ticket_price) - concert.expenses):.2f}$" \
               f" from the {concert.genre} concert in {concert_place}."

    def valid_band(self, band_name):
        band = next((b for b in self.bands if b.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        return band
