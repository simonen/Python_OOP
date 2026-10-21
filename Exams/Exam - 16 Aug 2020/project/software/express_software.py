from project.software.software import Software


class ExpressSoftware(Software):
    _TYPE = "Express"
    _MEM_CONSUM_FACTOR = 2
    _CAP_CONSUM_FACTOR = 1