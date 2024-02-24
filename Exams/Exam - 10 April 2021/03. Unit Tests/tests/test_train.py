from unittest import TestCase, main
from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train('BDZ', 100)

    def test_constructor(self):
        self.assertEqual((self.train.name, self.train.capacity, self.train.passengers), ('BDZ', 100, []))

    def test_add_no_capacity_exc(self):
        passenger = 'Gan4o'
        self.train.capacity = 2
        self.train.passengers = ['Pen4o', 'Dragan4o']

        with self.assertRaises(ValueError) as ve:
            self.train.add(passenger)

        res = self.train.passengers
        exp_res = ['Pen4o', 'Dragan4o']

        self.assertEqual(str(ve.exception), "Train is full")
        self.assertEqual(res, exp_res)

    def test_add_user_already_in_exc(self):
        passenger = 'Pen4o'
        self.train.capacity = 3
        self.train.passengers = ['Pen4o', 'Dragan4o']

        with self.assertRaises(ValueError) as ve:
            self.train.add(passenger)

        res = self.train.passengers
        exp_res = ['Pen4o', 'Dragan4o']

        self.assertEqual(str(ve.exception), f"Passenger {passenger} Exists")
        self.assertEqual(res, exp_res)

    def test_add(self):
        passenger = 'Mutragen'

        message = self.train.add(passenger)

        res = self.train.passengers
        exp_res = [passenger]

        self.assertEqual(message, f"Added passenger {passenger}")
        self.assertEqual(res, exp_res)

    def test_remove_no_passenger_exc(self):
        self.train.passengers = ['Pen4o']
        passenger = 'Trai4o'

        with self.assertRaises(ValueError) as ve:
            self.train.remove(passenger)

        self.assertEqual(str(ve.exception), "Passenger Not Found")
        self.assertEqual(self.train.passengers, ['Pen4o'])

    def test_remove(self):
        self.train.passengers = ['Pen4o', 'Dragan4o', 'Trai4o']
        passenger = 'Trai4o'

        message = self.train.remove(passenger)

        res = self.train.passengers
        exp_res = ['Pen4o', 'Dragan4o']

        self.assertEqual(message, f"Removed {passenger}")
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()