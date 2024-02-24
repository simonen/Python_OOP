from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TruckDriverTest(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('Pesho', 10.2)

    def test_constructor(self):
        name = self.driver.name
        rate = self.driver.money_per_mile
        cargo = self.driver.available_cargos
        money = self.driver.earned_money
        miles = self.driver.miles

        res = (name, rate, cargo, money, miles)
        exp_res = ('Pesho', 10.2, {}, 0, 0)

        self.assertEqual(res, exp_res)

    def test_earned_money_negative_raise_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Pesho went bankrupt.", str(ve.exception))

    def test_cargo_offer_already_added_raise_exc(self):
        self.driver.available_cargos = {'Paris': 1200}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Paris', 1201)

        res = self.driver.available_cargos
        exp_res = {'Paris': 1200}

        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.assertEqual(res, exp_res)

    def test_cargo_added(self):
        message = self.driver.add_cargo_offer('Paris', 1000)

        res = self.driver.available_cargos
        exp_res = {'Paris': 1000}

        self.assertEqual(res, exp_res)
        self.assertEqual(message, "Cargo for 1000 to Paris was added as an offer.")

    def test_drive_best_cargo_offer_no_offers_exception(self):
        self.driver.available_cargos = {}
        self.driver.miles = 0

        message = self.driver.drive_best_cargo_offer()

        self.assertEqual(message, "There are no offers available.")
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_drive_best_cargo_offer(self):
        self.driver.available_cargos = {'Dobrich': 10000, 'Pari6': 9999}

        message = self.driver.drive_best_cargo_offer()

        miles_res = self.driver.miles
        earned_money = self.driver.earned_money
        exp_earned_money = 102_000 - 450 - 3000 - 7500 - 800

        self.assertEqual(miles_res, 10000)
        self.assertEqual(earned_money, exp_earned_money)
        self.assertEqual(message, "Pesho is driving 10000 to Dobrich.")

    def test_eat(self):
        self.driver.earned_money = 1000
        self.driver.eat(1000)

        res_money = self.driver.earned_money

        self.assertEqual(res_money, 1000 - 20)

    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)

        res_money = self.driver.earned_money

        self.assertEqual(res_money, 1000 - 45)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(3000)

        res_money = self.driver.earned_money

        self.assertEqual(res_money, 1000 - 500)

    def test_repair_truck(self):
        self.driver.earned_money = 8000
        self.driver.repair_truck(20000)

        res_money = self.driver.earned_money

        self.assertEqual(res_money, 8000 - 7500)

    def test_repr_override(self):
        res = self.driver

        self.assertEqual(str(res), "Pesho has 0 miles behind his back.")


if __name__ == '__main__':
    main()