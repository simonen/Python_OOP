from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):
    def setUp(self) -> None:
        self.paint = PaintFactory('Moore', 10)

    def test_constructor(self):
        self.assertEqual(self.paint.name, 'Moore')
        self.assertEqual(self.paint.capacity, 10)
        self.assertEqual(self.paint.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.paint.ingredients, {})

    def test_add_ingredient_no_space_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.paint.add_ingredient("white", 12)

        res = self.paint.ingredients
        exp_res = {}

        self.assertEqual(str(ve.exception), "Not enough space in factory")
        self.assertEqual(res, exp_res)

    def test_add_ingredient_invalid_ingredint_te(self):
        product_type = 'hmel'
        with self.assertRaises(TypeError) as te:
            self.paint.add_ingredient(product_type, 19)

        res = self.paint.ingredients
        exp_res = {}

        self.assertEqual(str(te.exception), f"Ingredient of type {product_type} not allowed in PaintFactory")
        self.assertEqual(res, exp_res)

    def test_add_ingredient_valid_non_existent(self):
        self.paint.ingredients = {'red': 2}
        product_type = 'white'
        quantity = 5

        self.paint.add_ingredient(product_type, quantity)

        res = self.paint.ingredients
        exp_res = {'red': 2, 'white': 5}

        self.assertEqual(res, exp_res)

    def test_add_ingredient_valid_existent(self):
        self.paint.ingredients = {'white': 2}
        product_type = 'white'
        quantity = 5

        self.paint.add_ingredient(product_type, quantity)

        res = self.paint.ingredients
        exp_res = {'white': 7}

        self.assertEqual(res, exp_res)

    def test_remove_ingredient_less_than_zero_ve(self):
        self.paint.ingredients = {'white': 2}
        product = 'white'
        quantity = 12

        with self.assertRaises(ValueError) as ve:
            self.paint.remove_ingredient(product, quantity)

        self.assertEqual(str(ve.exception), "Ingredients quantity cannot be less than zero")

    def test_remove_ingredient_no_such_ingredient_ke(self):
        self.paint.ingredients = {'white': 2}
        product = 'qwa'
        quantity = 12

        with self.assertRaises(KeyError) as ke:
            self.paint.remove_ingredient(product, quantity)

        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient(self):
        self.paint.ingredients = {'white': 2}
        product = 'white'
        quantity = 2

        self.paint.remove_ingredient(product, quantity)

        res = self.paint.ingredients
        exp_res = {'white': 0}

        self.assertEqual(res, exp_res)

    def test_products(self):
        self.assertEqual(self.paint.products, {})


if __name__ == '__main__':
    main()