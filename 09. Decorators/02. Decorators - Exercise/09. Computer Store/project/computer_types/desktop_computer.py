from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }
    MAX_RAM = 128
    VALID_RAM_SIZE = {2 ** x: x * 100 for x in range(1, 8)}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAM_SIZE:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer"
                             f" {self.manufacturer} {self.model}!")

        self.price += self.PROCESSORS[processor]
        self.price += self.VALID_RAM_SIZE[ram]
        self.ram = ram
        self.processor = processor

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
