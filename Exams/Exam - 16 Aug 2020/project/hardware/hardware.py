from project.software.software import Software


class Hardware:
    _TYPE: str
    _CAP_FACTOR: float
    _MEM_FACTOR: float

    def __init__(self, name: str, capacity: int, memory: int) -> None:
        self.name = name
        self.hardware_type = self._TYPE
        self.capacity = int(capacity * self._CAP_FACTOR)
        self.memory = int(memory * self._MEM_FACTOR)
        self.software_components: list[Software] = []

    def install(self, software: Software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software) -> None:
        self.software_components.remove(software)