from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _VALID_SOFTWARE = {"Express": ExpressSoftware, "Light": LightSoftware}

    _hardware: list[Hardware] = []
    _software: list[Software] = []

    @staticmethod
    def _find_hardware(hardware_name: str):
        return next((x for x in System._hardware if x.name == hardware_name), None)

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int) -> None:
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int) -> None:
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_software(hardware_name: str, name: str, capacity_consumption: int,
                          memory_consumption: int, software_type: str) -> str | None:
        hardware = System._find_hardware(hardware_name)
        if hardware is None:
            return "Hardware does not exist"

        software = System._VALID_SOFTWARE[software_type](name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_express_software(hardware_name: str, name: str,
                                  capacity_consumption: int, memory_consumption: int) -> str | None:
        return System.register_software(hardware_name, name, capacity_consumption, memory_consumption, "Express")

    @staticmethod
    def register_light_software(hardware_name: str, name: str,
                                capacity_consumption: int, memory_consumption: int) -> str | None:
        return System.register_software(hardware_name, name, capacity_consumption, memory_consumption, "Light")

    @staticmethod
    def analyze() -> str:
        res = ["System Analysis", f"Hardware Components: {len(System._hardware)}", f"Software Components: {len(System._software)}",
               f"Total Operational Memory: {sum(x.memory_consumption for x in System._software)} / {sum(x.memory for x in System._hardware)}",
               f"Total Capacity Taken: {sum(x.capacity_consumption for x in System._software)} / {sum(x.capacity for x in System._hardware)}"]
        return "\n".join(res)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str) -> str | None:
        hardware = System._find_hardware(hardware_name)
        software = next((x for x in System._software if x.name == software_name), None)
        if hardware is None or software is None:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def system_split() -> str:
        res = []
        for hardware in System._hardware:
            res.append(f"Hardware Component - {hardware.name}")
            res.append(f"Express Software Components: {len([s for s in hardware.software_components if s.software_type == 'Express'])}")
            res.append(f"Light Software Components: {len([s for s in hardware.software_components if s.software_type == "Light"])}")
            res.append(f"Memory Usage: {sum(s.memory_consumption for s in hardware.software_components)} / {hardware.memory}")
            res.append(f"Capacity Usage: {sum(s.capacity_consumption for s in hardware.software_components)} / {hardware.capacity}")
            res.append(f"Type: {hardware.hardware_type}")
            res.append(f"Software Components: {', '.join(s.name for s in hardware.software_components) if len(hardware.software_components) > 0 else 'None'}")

        return '\n'.join(res)
