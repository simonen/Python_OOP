from unittest import TestCase, main
from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team('Malinka')

    def test_constructor(self):
        self.assertEqual((self.team.name, self.team.members), ('Malinka', {}))

    def test_name_non_letters_exc(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'M4linka'

        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member_not_present(self):
        self.team.members = {}
        message = self.team.add_member(Pen4o=10, Gan4o=100)

        res = self.team.members
        exp_res = {'Pen4o': 10, 'Gan4o': 100}

        self.assertEqual(message, f"Successfully added: Pen4o, Gan4o")
        self.assertEqual(res, exp_res)

        self.team.members = {'Pen4o': 10, 'Gan4o': 100}
        message2 = self.team.add_member(Men4o=10, Tan4o=100)

        res2 = self.team.members
        exp_res2 = {'Pen4o': 10, 'Gan4o': 100, 'Men4o': 10, 'Tan4o': 100}

        self.assertEqual(message2, f"Successfully added: Men4o, Tan4o")
        self.assertEqual(res2, exp_res2)

    def test_remove_member_non_existent(self):
        self.team.members = {'Pen4o': 10, 'Gan4o': 100}
        player = 'San4o'

        message = self.team.remove_member(player)

        res = self.team.members
        exp_res = {'Pen4o': 10, 'Gan4o': 100}

        self.assertEqual(message, f"Member with name {player} does not exist")
        self.assertEqual(res, exp_res)

    def test_remove_member(self):
        self.team.members = {'Pen4o': 10, 'Gan4o': 100}
        player = 'Gan4o'

        message = self.team.remove_member(player)

        res = self.team.members
        exp_res = {'Pen4o': 10}

        self.assertEqual(message, f"Member {player} removed")
        self.assertEqual(res, exp_res)

    def test_gt_override(self):
        other = Team('Tapinka')
        other.members = {'Pen4o': 10, 'Gan4o': 100}
        self.team.members = {'Min4o': 10, 'Pan4o': 22, 'Lal4o': 12}

        res = self.team.__gt__(other)
        exp_res = True

        self.assertEqual(res, exp_res)

        other.members = {'Pen4o': 10, 'Gan4o': 100}
        self.team.members = {'Min4o': 10, 'Pan4o': 22}

        res2 = self.team.__gt__(other)
        exp_res2 = False

        self.assertEqual(res2, exp_res2)

        other.members = {'Pen4o': 10, 'Gan4o': 100, 'Kreten4o': 221}
        self.team.members = {'Min4o': 10, 'Pan4o': 22}

        res3 = self.team.__gt__(other)
        exp_res3 = False

        self.assertEqual(res3, exp_res3)

    def test_len_override(self):
        self.team.members = {'Min4o': 10, 'Pan4o': 22}

        res = self.team.__len__()
        exp_res = 2

        self.assertEqual(res, exp_res)

    def test_add_override(self):
        other = Team('Wagner')
        other.members = {'Pen4o': 10, 'Gan4o': 100, 'Kreten4o': 221}
        self.team.members = {'Min4o': 10, 'Pan4o': 22}

        new_team = self.team.__add__(other)

        res = new_team.members
        exp_res = {'Min4o': 10, 'Pan4o': 22, 'Pen4o': 10, 'Gan4o': 100, 'Kreten4o': 221}

        self.assertEqual(res, exp_res)
        self.assertEqual(new_team.name, 'MalinkaWagner')

    def test_str_override(self):
        self.team.members = {'Pen4o': 100, 'Gan4o': 100, 'Kreten4o': 221}

        res = str(self.team)
        exp_res = f"Team name: Malinka" \
                  f"\nMember: Kreten4o - 221-years old" \
                  f"\nMember: Gan4o - 100-years old" \
                  f"\nMember: Pen4o - 100-years old"

        self.assertEqual(res, exp_res)

if __name__ == '__main__':
    main()