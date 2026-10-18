from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    MAX_MILEAGE: float
    """max_mileage attribute required for base class?"""
    def __init__(self, brand: str, model: str, license_plate_number: str) -> None:
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = self.MAX_MILEAGE
        self.battery_level: int = 100
        self.is_damaged: bool = False

    @abstractmethod
    def drive(self, mileage: float):
        ...

    @staticmethod
    def is_valid(string) -> bool:
        if string.strip():
            return True
        return False

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if not self.is_valid(value):
            raise ValueError("Brand cannot be empty!")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if not self.is_valid(value):
            raise ValueError("Model cannot be empty!")
        self._model = value

    @property
    def license_plate_number(self):
        return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value: str):
        if not self.is_valid(value):
            raise ValueError("License plate number is required!")
        self._license_plate_number = value

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        if self.is_damaged:
            self.is_damaged = False
        else:
            self.is_damaged = True

    def __str__(self) -> str:
        status = "Damaged" if self.is_damaged else "OK"
        return (f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery:"
                f" {self.battery_level}% Status: {status}")
