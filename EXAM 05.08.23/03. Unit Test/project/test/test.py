from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class SecondHandCarTest(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar('BMW', 'Car', 102, 1000)

    def test_constructor(self):
        model = self.car.model
        car_type = self.car.car_type
        miles = self.car.mileage
        price = self.car.price

        self.assertEqual((model, car_type, miles, price), ('BMW', 'Car', 102, 1000))

    def test_price_greater_than_1_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

    def test_mileage_less_than_100_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_promotional_price_higher_price_exc(self):
        new_price = 2000
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(new_price)

        res = self.car.price
        exp_price = 1000

        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')
        self.assertEqual(res, exp_price)

    def test_promotional_price(self):
        new_price = 900

        message = self.car.set_promotional_price(new_price)

        res = self.car.price
        exp_res = new_price

        self.assertEqual(message, 'The promotional price has been successfully set.')
        self.assertEqual(res, exp_res)

    def test_need_repair_impossible(self):
        repair_price = 600
        repair_description = 'wheels'

        message = self.car.need_repair(repair_price, repair_description)

        res_price = self.car.price
        exp_res_price = 1000
        res_repairs = self.car.repairs
        exp_repairs = []

        self.assertEqual(message, 'Repair is impossible!')
        self.assertEqual(res_price, exp_res_price)
        self.assertEqual(res_repairs, exp_repairs)

    def test_need_repair(self):
        repair_price = 400
        repair_description = 'wheels'

        message = self.car.need_repair(repair_price, repair_description)

        res_price = self.car.price
        exp_res_price = 1000 + 400
        res_repairs = self.car.repairs
        exp_repairs = [repair_description]

        self.assertEqual(message, f'Price has been increased due to repair charges.')
        self.assertEqual(res_price, exp_res_price)
        self.assertEqual(res_repairs, exp_repairs)

    def test_gt_override_type_mismatch(self):
        other = SecondHandCar('Mercedex', 'Truck', 1000, 3000)

        message = self.car > other

        self.assertEqual(message, 'Cars cannot be compared. Type mismatch!')

    def test_gt_override_type(self):
        other = SecondHandCar('Mercedex', 'Car', 1000, 3000)

        message = self.car > other

        self.assertEqual(message, False)

    def test_gt_override_type_2(self):
        other = SecondHandCar('Mercedex', 'Car', 1000, 900)

        message = self.car > other

        self.assertEqual(message, True)

    def test_str_override(self):
        self.car.repairs = ['wheels']
        res = str(self.car)
        exp_res = f"""Model BMW | Type Car | Milage 102km
Current price: 1000.00 | Number of Repairs: 1"""

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()
