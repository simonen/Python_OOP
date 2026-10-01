from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):

    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, milliliters: {self.milliliters}, caffeine: {self.caffeine}"
