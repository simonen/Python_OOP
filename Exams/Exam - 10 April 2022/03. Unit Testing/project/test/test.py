from unittest import TestCase, main
from project.movie import Movie


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Matrix', 1999, 10)

    def test_constructor(self):
        self.assertEqual((self.movie.name, self.movie.year, self.movie.rating, self.movie.actors),
                         ('Matrix', 1999, 10, []))

    def test_name_empty_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_invalid_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor_already_added(self):
        actor = 'Pen4o'
        self.movie.actors = ['Pen4o']

        message = self.movie.add_actor(actor)
        res = self.movie.actors
        exp_res = ['Pen4o']

        self.assertEqual(res, exp_res)
        self.assertEqual(message, f"{actor} is already added in the list of actors!")

    def test_add_actor(self):
        actor = 'Gan4o'
        self.movie.actors = ['Pen4o']

        self.movie.add_actor(actor)

        res = self.movie.actors
        exp_res = ['Pen4o', 'Gan4o']

        self.assertEqual(res, exp_res)

    def test_gt_override(self):
        other = Movie('Matrix 2', 2001, 9.9)
        other2 = Movie('Matrix 3', 2003, 11)

        message = self.movie.__gt__(other)
        message2 = self.movie.__gt__(other2)

        self.assertEqual(message, f'"Matrix" is better than "Matrix 2"')
        self.assertEqual(message2, f'"Matrix 3" is better than "Matrix"')

    def test_repr_override(self):
        self.movie.rating = 9.12
        self.movie.actors = ['Keano', 'Meano']
        res = self.movie.__repr__()
        exp_res = f"Name: Matrix\n" \
                  f"Year of Release: 1999\n" \
                  f"Rating: 9.12\n" \
                  f"Cast: Keano, Meano"

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()
