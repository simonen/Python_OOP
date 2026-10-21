from project.software.software import Software


class LightSoftware(Software):
    _TYPE = "Light"
    _MEM_CONSUM_FACTOR = 0.5
    _CAP_CONSUM_FACTOR = 1.5

