class Software:

    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        self.name = name
        self.software_type = software_type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    def __repr__(self):
        return f"Name: {self.name}, Type: {self.software_type}, Cap: {self.capacity_consumption}, Mem: {self.memory_consumption}"
