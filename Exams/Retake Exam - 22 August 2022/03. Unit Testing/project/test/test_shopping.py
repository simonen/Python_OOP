from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class ShoppingCartTest(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart('Chikoto', 1000)

    def test_constructor(self):
        name = self.cart.shop_name
        budget = self.cart.budget
        products = self.cart.products

        res = (name, budget, products)
        exp_res = ('Chikoto', 1000, {})

        self.assertEqual(res, exp_res)

    def test_shop_name_no_uppercase_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'chiko'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_non_alpha_chars_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'Ch1k0'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_cost_too_much_exc(self):
        product = 'hleb'
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart(product, 100)

        res = self.cart.products
        exp_res = {}
        res_budget = self.cart.budget
        exp_budget = 1000

        self.assertEqual(res, exp_res)
        self.assertEqual(res_budget, exp_budget)
        self.assertEqual(f"Product {product} cost too much!", str(ve.exception))

    def test_add_to_cart(self):
        product = 'hlep'
        price = 99

        message = self.cart.add_to_cart(product, price)

        res = self.cart.products
        exp_res = {product: price}

        self.assertEqual(message, f"{product} product was successfully added to the cart!")
        self.assertEqual(res, exp_res)

    def test_remove_from_cart_no_product_exc(self):
        self.cart.products = {'Valfi': 5, 'Voda': 18}
        product = 'hlep'

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart(product)

        res = self.cart.products
        exp_res = {'Valfi': 5, 'Voda': 18}

        self.assertEqual(res, exp_res)
        self.assertEqual(f"No product with name {product} in the cart!", str(ve.exception))

    def test_remove_from_cart(self):
        product = 'Valfi'
        self.cart.products = {'Valfi': 5, 'Voda': 18}

        message = self.cart.remove_from_cart(product)

        res = self.cart.products
        exp_res = {'Voda': 18}

        self.assertEqual(message, f"Product {product} was successfully removed from the cart!")
        self.assertEqual(res, exp_res)

    def test_add_override(self):
        other = ShoppingCart('Mikoto', 400)
        other.products = {'Valfi': 5, 'Voda': 18}
        self.cart.products = {'Hlqp': 10, 'Mlqko': 13}

        new_cart = self.cart.__add__(other)

        res_name = new_cart.shop_name
        res_budget = new_cart.budget
        res_cart = new_cart.products

        exp_name = 'ChikotoMikoto'
        exp_budget = self.cart.budget + other.budget
        exp_cart = {'Hlqp': 10, 'Mlqko': 13, 'Valfi': 5, 'Voda': 18}

        res = res_name, res_budget, res_cart
        exp_res = exp_name, exp_budget, exp_cart

        self.assertEqual(res, exp_res)

    def test_buy_products_no_money_exc(self):
        self.cart.budget = 28
        self.cart.products = {'Hlqp': 10, 'Mlqko': 13, 'Valfi': 5, 'Voda': 18}

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with "
                         f"{sum(self.cart.products.values()) - self.cart.budget:.2f}lv!",
                         str(ve.exception))

    def test_buy_products(self):
        self.cart.products = {'Hlqp': 10, 'Mlqko': 13, 'Valfi': 5, 'Voda': 18}

        message = self.cart.buy_products()

        self.assertEqual(message, f'Products were successfully bought! '
                                  f'Total cost: {sum(self.cart.products.values()):.2f}lv.')


if __name__ == '__main__':
    main()