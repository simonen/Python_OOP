from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, dev1, dev2) -> str:
        return f"Connecting {dev1.__class__.__name__} to {dev2.__class__.__name__}"


class HDMICable(Cable):
    def connect(self, dev1, dev2) -> str:
        return f"{super().connect(dev1, dev2)} via HDMI"


class RCACable(Cable):
    def connect(self, dev1, dev2) -> str:
        return f"{super().connect(dev1, dev2)} via RCA"


class EthernetCable(Cable):
    def connect(self, dev1, dev2) -> str:
        return f"{super().connect(dev1, dev2)} via Ethernet"


class PowerCable(Cable):
    def connect(self, dev1, socket) -> str:
        return f"Connecting {dev1.__class__.__name__} to power socket"


class Device:
    pass


class PowerSocket:
    pass


class DVDPlayer(Device):
    pass


class GameConsole:
    pass


class Router:
    pass


class Television:
    pass


hdmi_cable = HDMICable()
dvd_player = DVDPlayer()
power_cable = PowerCable()
tv = Television()
power_socket = PowerSocket()
print(hdmi_cable.connect(dvd_player, tv))
print(power_cable.connect(dvd_player, power_socket))
g_console = GameConsole()
