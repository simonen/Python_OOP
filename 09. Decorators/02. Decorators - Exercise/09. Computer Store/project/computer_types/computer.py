from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        ...

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if not value.split():
            raise ValueError("Manufacturer name cannot be empty.")
        self._manufacturer = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if not value.split():
            raise ValueError("Model name cannot be empty.")
        self._model = value

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
