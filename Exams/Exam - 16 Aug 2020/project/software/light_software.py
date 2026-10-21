from project.software.software import Software


class LightSoftware(Software):
    _TYPE = "Light"
    _MEM_CONSUM_FACTOR = 0.5
    _CAP_CONSUM_FACTOR = 1.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self._TYPE, int(capacity_consumption * self._CAP_CONSUM_FACTOR),
                         int(memory_consumption * self._MEM_CONSUM_FACTOR))
