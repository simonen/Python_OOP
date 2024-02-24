from unittest import TestCase, main
from car_manager import Car


class CarTest(TestCase):
    def setUp(self) -> None:
        self.car = Car('BMW', 'Model X', 10, 50)

    def test_constructor_make_ok(self):
        make = self.car.make
        model = self.car.model
        fuel_cons = self.car.fuel_consumption
        fuel_cap = self.car.fuel_capacity

        res = make, model, fuel_cons, fuel_cap
        exp_res = ('BMW', 'Model X', 10, 50)

        self.assertEqual(exp_res, res)

    def test_constructor_make_raise_ex(self):
        with self.assertRaises(Exception) as ex:
            Car('', 'Model X', 10, 50)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_constructor_model_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            Car('BMW', '', 10, 50)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_constructor_fuel_consumption_raises_exc(self):
        with self.assertRaises(Exception) as ex:
            Car('BMW', 'Model X', 0, 50)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption(self):
        fuel_cons = self.car.fuel_consumption
        self.assertEqual(10, fuel_cons)

    def test_fuel_consumption_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_constructor_fuel_capacity_raises_exc(self):
        with self.assertRaises(Exception) as ex:
            Car('BMW', 'Model X', 11, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raises_exc(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        fuel_cap = self.car.fuel_capacity
        self.assertEqual(50, fuel_cap)

    def test_fuel_amount_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_ok(self):
        self.car.fuel_amount = 10
        res = self.car.fuel_amount
        exp_res = 10

        self.assertEqual(exp_res, res)

    def test_refuel_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_over_capacity(self):
        self.car.refuel(60)
        curr_fuel = self.car.fuel_amount

        if curr_fuel > self.car.fuel_capacity:
            self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel(self):
        fuel = self.car.fuel_amount
        self.car.refuel(10)

        res = self.car.fuel_amount
        exp_res = fuel + 10

        self.assertEqual(exp_res, res)

    def test_drive_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        self.car.fuel_amount = 10
        self.car.drive(100)

        res = self.car.fuel_amount
        exp_res = 0

        self.assertEqual(exp_res, res)


if __name__ == "__main__":
    main()
