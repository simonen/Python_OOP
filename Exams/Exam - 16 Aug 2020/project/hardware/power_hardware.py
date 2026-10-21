from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _TYPE = 'Power'
    _CAP_FACTOR = 0.25
    _MEM_FACTOR = 1.75