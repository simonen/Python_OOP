from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CARS = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: list[Car] = []
        self.drivers: list[Driver] = []
        self.races: list[Race] = []

    def _find_driver(self, driver_name: str) -> Driver | None:
        return next((x for x in self.drivers if x.name == driver_name), None)

    def _find_race(self, race_name: str) -> Race | None:
        return next((x for x in self.races if x.name == race_name), None)

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in Controller.VALID_CARS:
            return None

        if any(x for x in self.cars if x.model == model):
            raise Exception(f"Car {model} is already created!")

        car = Controller.VALID_CARS[car_type](model, speed_limit)
        self.cars.append(car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._find_driver(driver_name) is not None:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._find_race(race_name) is not None:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type not in Controller.VALID_CARS:
            raise Exception(f"Car {car_type} could not be found!")

        car = next((x for x in reversed(self.cars) if isinstance(x, Controller.VALID_CARS[car_type]) and not x.is_taken), None)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        car.is_taken = True

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._find_race(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self._find_driver(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._find_race(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_car_desc = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        top_3 = fastest_car_desc[:3]

        res = []
        for driver in top_3:
            driver.number_of_wins += 1
            res += [f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}."]

        return "\n".join(res)

    # def add_car_to_driver(self, ...): Validate the car_type inside the next() with default dict value .get(car_type, type(None))
    #     car = next(
    #         (i for i in self.cars[::-1] if isinstance(i, self.VALID_CARS.get(car_type, type(None))) and not i.is_taken),
    #         None)
    #     if car_type not in self.VALID_CARS or car is None or all(x.is_taken for x in self.cars):
    #         raise Exception(f"Car {car_type} could not be found!")