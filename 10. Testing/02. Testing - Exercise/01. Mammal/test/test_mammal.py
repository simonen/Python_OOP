from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal(
            'some name',
            'some type',
            'some sound'
        )

    def test_constructor(self):
        res = (self.mammal.name, self.mammal.type, self.mammal.sound)
        exp_res = ('some name', 'some type', 'some sound')

        self.assertEqual(exp_res, res)

    def test_make_sound(self):
        res = self.mammal.make_sound()
        exp_res = 'some name makes some sound'

        self.assertEqual(exp_res, res)

    def test_get_kingdom(self):
        res = self.mammal.get_kingdom()
        exp_res = "animals"

        self.assertEqual(exp_res, res)

    def test_info(self):
        res = self.mammal.info()
        exp_res = 'some name is of type some type'

        self.assertEqual(exp_res, res)


if __name__ == '__main__':
    main()