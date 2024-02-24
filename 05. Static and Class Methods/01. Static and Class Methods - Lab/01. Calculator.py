from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 4))
print(Calculator.multiply(4, 12))
print(Calculator.divide(6, 2))
print(Calculator.subtract(5, 10))
