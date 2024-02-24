from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TennisPlayerTest(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Test', 21, 1000)

    def test_constructor(self):
        name = self.player.name
        age = self.player.age
        points = self.player.points

        res = (name, age, points)
        exp_res = ('Test', 21, 1000)

        self.assertEqual(res, exp_res)

    def test_name_less_than_two_raises_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Az'

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_less_than_18_raises_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 5

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_already_won(self):
        self.player.wins = ['Grand']

        message = self.player.add_new_win('Grand')
        res_wins = self.player.wins
        exp_wins = ['Grand']

        self.assertEqual(message, "Grand has been already added to the list of wins!")
        self.assertEqual(res_wins, exp_wins)

    def test_add_new_win(self):
        self.player.add_new_win("Grand")

        res = self.player.wins
        exp_res = ['Grand']

        self.assertEqual(res, exp_res)

    def test_lt_fewer_points(self):
        other = TennisPlayer('Test2', 21, 1001)

        message = self.player.__lt__(other)

        self.assertEqual(message, "Test2 is a top seeded player and he/she is better than Test")

    def test_lt_more_points(self):
        other = TennisPlayer('Test2', 21, 0)

        message = self.player.__lt__(other)

        self.assertEqual(message, "Test is a better player than Test2")

    def test_str_override(self):
        self.player.wins = ['Grand', '4urizo']
        res = str(self.player)
        exp_res = f"Tennis Player: Test\n" \
                  f"Age: 21\n" \
                  f"Points: 1000.0\n" \
                  f"Tournaments won: Grand, 4urizo"

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()
