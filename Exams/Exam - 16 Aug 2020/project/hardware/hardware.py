from typing import List
from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)




