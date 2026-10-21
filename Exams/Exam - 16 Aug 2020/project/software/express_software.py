from project.software.software import Software


class ExpressSoftware(Software):
    _TYPE = "Express"
    _MEM_CONSUM_FACTOR = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self._TYPE, capacity_consumption, int(memory_consumption * self._MEM_CONSUM_FACTOR))
