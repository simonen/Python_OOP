from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        valid_computers = {'Desktop Computer': DesktopComputer(manufacturer, model),
                           'Laptop': Laptop(manufacturer, model)}

        if type_computer not in valid_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = valid_computers[type_computer]
        computer.configure_computer(processor, ram)
        self.profits -= computer.price
        self.warehouse.append(computer)
        return f"Created {manufacturer} {model} with {processor} and {ram}GB RAM for {computer.price}$."

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        computer = next((x for x in self.warehouse if (x.price <= client_budget) and (x.processor == wanted_processor) and (x.ram >= wanted_ram)), None)
        if not computer:
            raise Exception(f"Sorry, we don't have a computer for you.")

        self.profits += (client_budget - computer.price)
        self.warehouse.remove(computer)
        return f"{computer} sold for {client_budget}$."
