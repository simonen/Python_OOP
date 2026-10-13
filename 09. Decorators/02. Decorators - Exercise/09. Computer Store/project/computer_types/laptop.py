from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }
    MAX_RAM = 64
    VALID_RAM_SIZE = {2 ** x: x * 100 for x in range(1, 7)}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAM_SIZE:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.price += self.PROCESSORS[processor]
        self.price += self.VALID_RAM_SIZE[ram]
        self.ram = ram
        self.processor = processor
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
