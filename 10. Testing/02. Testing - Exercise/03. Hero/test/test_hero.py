from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Some Name', 99, 100, 15)

    def test_constructor(self):
        username = self.hero.username
        level = self.hero.level
        health = self.hero.health
        damage = self.hero.damage

        res = (username, level, health, damage)
        exp_res = ('Some Name', 99, 100, 15)

        self.assertEqual(exp_res, res)

    def test_battle_self_fight_raises_exc(self):
        self.enemy = Hero('Some Name', 1, 100, 21)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_below_zero_raises_exc(self):
        self.enemy = Hero('Pen4o', 1, 100, 21)
        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_below_0_raises_exc(self):
        self.enemy = Hero('Pen4o', 1, 0, 21)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_hero_wins(self):
        self.enemy = Hero('Pen4o', 1, 100, 21)
        enemy_damage = 21 * 1
        hero_start_health = self.hero.health
        hero_start_level = self.hero.level
        hero_start_damage = self.hero.damage
        message = self.hero.battle(self.enemy)
        res_health = self.hero.health
        exp_res_health = hero_start_health - enemy_damage + 5
        res_level = self.hero.level
        exp_res_level = hero_start_level + 1
        res_damage = self.hero.damage
        exp_res_damage = hero_start_damage + 5
        exp_message = 'You win'

        self.assertEqual(exp_res_health, res_health)
        self.assertEqual(exp_res_level, res_level)
        self.assertEqual(exp_res_damage, res_damage)
        self.assertEqual(message, exp_message)

    def test_battle_hero_lose(self):
        self.enemy = Hero('Pen4o', 5, 100, 21)
        self.hero.level = 5
        hero_damage = 5 * 15
        enemy_start_health = self.enemy.health
        enemy_start_level = self.enemy.level
        enemy_start_damage = self.enemy.damage
        message = self.hero.battle(self.enemy)
        res_health = self.enemy.health
        exp_res_health = enemy_start_health - hero_damage + 5
        res_level = self.enemy.level
        exp_res_level = enemy_start_level + 1
        res_damage = self.enemy.damage
        exp_res_damage = enemy_start_damage + 5
        exp_message = 'You lose'

        self.assertEqual(exp_res_health, res_health)
        self.assertEqual(exp_res_level, res_level)
        self.assertEqual(exp_res_damage, res_damage)
        self.assertEqual(message, exp_message)

    def test_battle_draw(self):
        self.enemy = Hero('Pen4o', 50, 100, 20)
        self.hero.level = 40

        start_hero_level = self.hero.level
        start_hero_damage = self.hero.damage

        start_enemy_level = self.enemy.level
        start_enemy_damage = self.enemy.damage

        # self.hero.battle(self.enemy)
        message = self.hero.battle(self.enemy)
        res_hero_level = self.hero.level
        res_hero_damage = self.hero.damage

        res_enemy_level = self.enemy.level
        res_enemy_damage = self.enemy.damage

        self.assertEqual(start_hero_level, res_hero_level)
        self.assertEqual(start_hero_damage, res_hero_damage)
        self.assertEqual(start_enemy_damage, res_enemy_damage)
        self.assertEqual(start_enemy_level, res_enemy_level)
        self.assertEqual(message, 'Draw')

    def test_string_override(self):
        res = str(self.hero)
        exp_res = f"Hero Some Name: 99 lvl\n" \
                  f"Health: 100\n" \
                  f"Damage: 15\n"

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()
