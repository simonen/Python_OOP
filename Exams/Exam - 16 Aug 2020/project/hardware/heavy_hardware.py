from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    _TYPE = 'Heavy'
    _CAP_FACTOR = 2
    _MEM_FACTOR = 0.75