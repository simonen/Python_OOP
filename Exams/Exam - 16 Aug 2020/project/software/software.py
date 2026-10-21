from abc import ABC


class Software(ABC):
    _TYPE: str
    _MEM_CONSUM_FACTOR: float
    _CAP_CONSUM_FACTOR: float

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int) -> None:
        self.name = name
        self.software_type = self._TYPE
        self.capacity_consumption = int(capacity_consumption * self._CAP_CONSUM_FACTOR)
        self.memory_consumption = int(memory_consumption * self._MEM_CONSUM_FACTOR)

    def __repr__(self):
        return f"Name: {self.name}, Type: {self.software_type}, Cap: {self.capacity_consumption}, Mem: {self.memory_consumption}"
