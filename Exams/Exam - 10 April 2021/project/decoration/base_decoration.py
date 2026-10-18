from abc import ABC


class BaseDecoration(ABC):
    def __init__(self, comfort: int, price: float) -> None:
        self.comfort = comfort
        self.price = price
