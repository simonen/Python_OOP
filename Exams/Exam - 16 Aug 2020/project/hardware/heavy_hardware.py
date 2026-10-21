from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    _TYPE = 'Heavy'
    _CAP_FACTOR = 2
    _MEM_FACTOR = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self._TYPE, capacity * self._CAP_FACTOR, int(memory * self._MEM_FACTOR))