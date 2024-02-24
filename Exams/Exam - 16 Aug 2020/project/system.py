from typing import List
from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.hardware import Hardware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    def __init__(self):
        pass

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int) -> None:
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int) -> None:
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @classmethod
    def software_register(cls, hardware_name: str, name: str,
                          capacity_consumption: int, memory_consumption: int, soft_type: str) -> str or None:

        hardware = next((h for h in System._hardware if h.name == hardware_name), None)
        if not hardware:
            return "Hardware does not exist"

        software = globals()[soft_type](name, capacity_consumption, memory_consumption)

        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_express_software(hardware_name: str, name: str,
                                  capacity_consumption: int, memory_consumption: int) -> str or None:

        return System.software_register(hardware_name, name, capacity_consumption, memory_consumption, 'ExpressSoftware')

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int) -> str or None:

        return System.software_register(hardware_name, name, capacity_consumption, memory_consumption, 'LightSoftware')

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str) -> str or None:
        try:
            hardware = next(h for h in System._hardware if h.name == hardware_name)
            software = next(s for s in hardware.software_components if s.name == software_name)
        except StopIteration:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze() -> str:

        res = f"System Analysis" \
              f"\nHardware Components: {len(System._hardware)}" \
              f"\nSoftware Components: {len(System._software)}" \
              f"\nTotal Operational Memory: {sum(x.memory_consumption for x in System._software)} / " \
              f"{sum(x.memory for x in System._hardware)}" \
              f"\nTotal Capacity Taken: {sum(x.capacity_consumption for x in System._software)} / " \
              f"{sum(x.capacity for x in System._hardware)}"

        return res

    @staticmethod
    def system_split() -> str:
        res = []
        for hardware in System._hardware:
            express_software = list(filter(lambda x: x.software_type == 'Express', hardware.software_components))
            light_software = list(filter(lambda x: x.software_type == 'Light', hardware.software_components))
            res.append(f"Hardware Component - {hardware.name}")
            res.append(f"Express Software Components: {len(express_software)}")
            res.append(f"Light Software Components: {len(light_software)}")
            res.append(
                f"Memory Usage: {sum(x.memory_consumption for x in hardware.software_components)} / {hardware.memory}")
            res.append(
                f"Capacity Usage: {sum(x.capacity_consumption for x in hardware.software_components)} / {hardware.capacity}")
            res.append(f"Type: {hardware.hardware_type}")
            res.append(
                f"Software Components: {', '.join(x.name for x in hardware.software_components) if hardware.software_components else 'None'}")

        return '\n'.join(res)
