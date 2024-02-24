from unittest import TestCase, main
from project.toy_store import ToyStore


class ToyStoreTest(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_constructor(self):
        toy_shelf = self.store.toy_shelf

        res = toy_shelf
        exp_res = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual(res, exp_res)

    def test_add_toy_no_shelf_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('Q', 'Doll')

        res = self.store.toy_shelf
        exp_res = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(res, exp_res)

    def test_add_toy_already_in_shelf_exc(self):
        self.store.toy_shelf['A'] = 'Doll'

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", 'Doll')

        res = self.store.toy_shelf
        exp_res = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual(res, exp_res)
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_taken_shelf_exc(self):
        self.store.toy_shelf['A'] = 'Doll'

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", 'Moll')

        res = self.store.toy_shelf
        exp_res = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual(res, exp_res)
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy(self):
        message = self.store.add_toy("B", 'Dolly')

        res = self.store.toy_shelf
        exp_res = {"A": None, "B": 'Dolly', "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual(message, "Toy:Dolly placed successfully!")
        self.assertEqual(res, exp_res)

    def test_remove_toy_no_shelf_exc(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('Q', 'Doll')

        res = self.store.toy_shelf
        exp_res = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(res, exp_res)

    def test_remove_toy_no_toy_exc(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'Doll')

        res = self.store.toy_shelf
        exp_res = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual(res, exp_res)

    def test_remove_toy(self):
        self.store.toy_shelf = {"A": None, "B": 'Dolly', "C": None, "D": None, "E": None, "F": None, "G": None}

        message = self.store.remove_toy('B', 'Dolly')

        res = self.store.toy_shelf
        exp_res = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual(message, "Remove toy:Dolly successfully!")
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()