from unittest import TestCase, main
from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet = PetShop('Doggo')

    def test_constructor(self):
        self.assertEqual((self.pet.name, self.pet.food, self.pet.pets), ('Doggo', {}, []))

    def test_add_food_quantity_exc(self):
        food = 'trici'
        quantity = 0
        with self.assertRaises(ValueError) as ve:
            self.pet.add_food(food, quantity)

        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')
        res = self.pet.food
        exp_res = {}

        self.assertEqual(res, exp_res)

    def test_add_food(self):
        food = 'trici'
        quantity = 10.21

        message = self.pet.add_food(food, quantity)

        res = self.pet.food
        exp_res = {food: quantity}

        self.assertEqual(message, f"Successfully added {quantity:.2f} grams of {food}.")
        self.assertEqual(res, exp_res)

    def test_add_pet_same_name_exc(self):
        self.pet.pets = ['Pen4o', 'A4o']
        name = 'Pen4o'
        with self.assertRaises(Exception) as ex:
            self.pet.add_pet(name)

        self.assertEqual(self.pet.pets, ['Pen4o', 'A4o'])
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_add_pet(self):
        self.pet.pets = ['Pen4o', 'A4o']
        name = 'Ten4o'

        message = self.pet.add_pet(name)

        res = self.pet.pets
        exp_res = ['Pen4o', 'A4o', 'Ten4o']

        self.assertEqual(message, f"Successfully added {name}.")
        self.assertEqual(res, exp_res)

    def test_feed_pet_invalid_name_exc(self):
        self.pet.pets = ['Pen4o', 'A4o']
        self.pet.food = {'Trici': 100}
        name = 'Ten4o'
        food = 'Trici'

        with self.assertRaises(Exception) as ex:
            self.pet.feed_pet(food, name)

        res = self.pet.food
        exp_res = {'Trici': 100}

        self.assertEqual(str(ex.exception), "Please insert a valid pet name")
        self.assertEqual(res, exp_res)

    def test_feed_pet_no_food(self):
        self.pet.pets = ['Pen4o', 'A4o']
        self.pet.food = {'Trici': 100}
        name = 'Pen4o'
        food = 'Qrma'

        message = self.pet.feed_pet(food, name)

        res = self.pet.food
        exp_res = {'Trici': 100}

        self.assertEqual(message, f'You do not have {food}')
        self.assertEqual(res, exp_res)

    def test_feed_pet_food_below_100(self):
        self.pet.pets = ['Pen4o', 'A4o']
        self.pet.food = {'Trici': 90}
        name = 'Pen4o'
        food = 'Trici'

        message = self.pet.feed_pet(food, name)

        res = self.pet.food
        exp_res = {'Trici': 1090}

        self.assertEqual(message, "Adding food...")
        self.assertEqual(res, exp_res)

    def test_feed_pet(self):
        self.pet.pets = ['Pen4o', 'A4o']
        self.pet.food = {'Trici': 110}
        name = 'Pen4o'
        food = 'Trici'

        message = self.pet.feed_pet(food, name)

        res = self.pet.food
        exp_res = {'Trici': 10}

        self.assertEqual(message, f"{name} was successfully fed")
        self.assertEqual(res, exp_res)

    def test_repr_override(self):
        self.pet.pets = ['Pen4o', 'A4o']

        res = self.pet.__repr__()
        exp_res = f'Shop Doggo:\n' \
                  f'Pets: Pen4o, A4o'

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()
