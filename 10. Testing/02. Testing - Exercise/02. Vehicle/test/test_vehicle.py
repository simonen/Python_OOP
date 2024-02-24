from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def setUp(self) -> None:
        self.car = Vehicle(70, 130)

    def test_constructor(self):
        fuel = self.car.fuel
        hp = self.car.horse_power
        res = (fuel, hp)
        exp_res = (70, 130)

        self.assertEqual(exp_res, res)

    def test_drive_no_fuel_raise_exc(self):
        self.car.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(1)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        start_fuel = self.car.fuel
        self.car.drive(8)

        res = self.car.fuel
        exp_res = start_fuel - 10

        self.assertEqual(exp_res, res)

    def test_refuel_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.car.fuel = 60
        start_fuel = self.car.fuel

        self.car.refuel(10)
        res = self.car.fuel
        exp_res = start_fuel + 10

        self.assertEqual(exp_res, res)

    def test_str(self):
        res = self.car
        exp_res = f"The vehicle has 130 " \
               f"horse power with 70 fuel left and 1.25 fuel consumption"

        self.assertEqual(exp_res, str(res))


if __name__ == '__main__':
    main()