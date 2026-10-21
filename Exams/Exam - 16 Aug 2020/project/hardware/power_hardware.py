from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _TYPE = 'Power'
    _CAP_FACTOR = 0.25
    _MEM_FACTOR = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self._TYPE, int(capacity * self._CAP_FACTOR), int(memory * self._MEM_FACTOR))
