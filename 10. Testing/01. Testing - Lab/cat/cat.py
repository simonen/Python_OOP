class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Pen4o')

    def test_size_increase_eat(self):
        start_size = self.cat.size
        self.cat.eat()
        res = self.cat.size
        exp_res = start_size + 1
        self.assertEqual(exp_res, res)

    def test_car_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat_after_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception.args[0]))

    def test_cat_sleep_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception.args[0]))

    def test_cat_not_sleepy_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()