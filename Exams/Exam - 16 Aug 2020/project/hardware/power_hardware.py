from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', capacity, memory)
        self.capacity = (capacity * 25) // 100
        self.memory = (memory * 175) // 100
