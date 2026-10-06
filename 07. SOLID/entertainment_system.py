from abc import ABC


class Device(ABC):
    PORTS: list[str] = []

    @property
    def ports(self) -> list[str]:
        return ['Power'] + type(self).PORTS # == Subclass.PORTS "coz this is class level attr"

    def __repr__(self):
        return self.__class__.__name__


class Cable(ABC):

    PORT:str | None = None    # Either a string or None but fall back to None if nothing

    @classmethod
    def connect(cls, dev1:Device, dev2: Device) -> str:

        if cls.PORT not in dev1.ports:
            return f"{dev1} has no {cls.PORT} ports"
        if cls.PORT not in dev2.ports:
            return f"{dev2} has no {cls.PORT} ports"

        return (f"{dev1} connected to"
                f" {dev2} via {cls.PORT}")


class HDMI(Cable):
    PORT: str = 'HDMI'


class Power(Cable):
    PORT = 'Power'


class Ethernet(Cable):
    PORT = 'Ethernet'


class Router(Device):
    PORTS = ['Ethernet']


class TV(Device):
    PORTS = ['HDMI', 'Ethernet']


tv = TV()
router = Router()
hdmi = HDMI()
power = Power()
ether = Ethernet()
print(ether.PORT)

# print(hdmi.connect(tv, router))
print(ether.connect(tv, router))
print(tv)
print(tv.ports)
# devi = Cable()
# print(devi)
