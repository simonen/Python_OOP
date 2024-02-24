from typing import List
from project.driver import Driver
from project.car.car import Car
from project.race import Race
from project.car.sports_car import SportsCar
from project.car.muscle_car import MuscleCar


class Controller:

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str or None:
        if any(c for c in self.cars if c.model == model):
            raise Exception(f"Car {model} is already created!")

        if car_type not in ['MuscleCar', 'SportsCar']:
            return None

        new_car = globals()[car_type](model, speed_limit)
        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str or None:
        if any(d for d in self.drivers if d.name == driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str or None:
        if any(r for r in self.races if r.name == race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str or None:
        car = next((c for c in self.cars[::-1] if c.__class__.__name__ == car_type and not c.is_taken), None)
        driver = next((d for d in self.drivers if d.name == driver_name), None)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        car.is_taken = True

        if driver.car:
            driver.car.is_taken = False
            old_model = driver.car.model
            new_model = car.model
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = next((r for r in self.races if r.name == race_name), None)
        driver = next((d for d in self.drivers if d.name == driver_name), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next((r for r in self.races if r.name == race_name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        ranking = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]
        winners = []

        for driver in ranking:
            driver.number_of_wins += 1
            winners.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(winners)
