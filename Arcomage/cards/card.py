from players.player import Player


class Card:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        # self.cost = cost

    def __repr__(self):
        return f"{self.title = }, {self.description = }, res {self.cost = }"

    @classmethod
    def damage(cls, player, structure: str, d: int):
        initial = player.kwargs[structure]
        player.kwargs[structure] += d
        t_damage = d
        if player.kwargs['wall'] < 0:
            t_damage = player.kwargs['wall']
            player.kwargs['wall'] = 0
            print(f"-{initial} {structure}")
            cls.damage(player, 'tower', t_damage)
        else:
            player.kwargs['tower'] = max(0, player.kwargs['tower'])
            print(f"{t_damage if player.kwargs['tower'] > 0 else initial} {structure}")

    @classmethod
    def resource(cls, player, res):
        for k, v in res.items():
            player.kwargs[k] += v

            if k in ['quarry', 'magic', 'dungeon'] and player.kwargs[k] < 1:
                player.kwargs[k] = 1
            elif k in ['bricks', 'gems', 'recruits'] and player.kwargs[k] < 0:
                player.kwargs[k] = 0

            print(f"{v} {k}")


class StripMine(Card):
    def __init__(self, players):
        title = "Strip Mine"
        description = "-1 Quarry, +10 Wall. You gain 5 gems"
        res = {"quarry": -1, "wall": 10}
        self.resource(players[0], res)
        cost = {"bricks": 0}
        super().__init__(title, description, cost)


class Foundations(Card):
    def __init__(self, players: list):
        title = "Foundations"
        description = "If wall = 0, +6 wall, else +3 wall"
        res = {"wall": 6} if players[0].kwargs['wall'] == 0 else {"wall": 3}
        self.resource(players[0], res)
        cost = {"bricks": 3}
        # Call the constructor of the parent class with preset values
        super().__init__(title, description, cost)


class LightningShard(Card):
    def __init__(self, players):
        title = "Lightning Shard"
        description = "If Tower > enemy wall, 8 damage to enemy tower. Else 8 damage"
        prop = 'tower' if players[0].kwargs['tower'] > players[1].kwargs['wall'] else 'wall'
        damage = -8
        self.damage(players[1], prop, damage)
        cost = {"gems": 11}

        super().__init__(title, description, cost)


class NewEquipment(Card):
    def __init__(self, players):
        # Preset values for Jack card
        title = "New Equipment"
        description = "+2 Quarry"
        res = {"quarry": 2}
        self.resource(players[0], res)
        cost = {"bricks": 6}
        super().__init__(title, description, cost)


class Succubus(Card):
    def __init__(self, players):
        title = "Succubus"
        description = "5 Damage to enemy tower, enemy loses 8 recruits"
        prop = "tower"
        damage = -5
        res = {'recruits': -8}
        self.damage(players[1], prop, damage)
        self.resource(players[1], res)
        cost = {"recruits": 14}
        super().__init__(title, description, cost)


class PearlOfWisdom(Card):
    def __init__(self, players):
        title = "Pearl of Wisdom"
        description = "+5 Tower. +1 Magic"
        res = {"tower": 5, "magic": 1}
        self.resource(players[0], res)
        cost = {"gems": 3}
        super().__init__(title, description, cost)


class Sapphire(Card):
    def __init__(self, players):
        title = "Sapphire"
        description = "+11 Tower"
        res = {"tower": 11}
        cost = {"gems": 10}
        self.resource(players[0], res)
        super().__init__(title, description, cost)


class Spearman(Card):
    def __init__(self, players):
        title = "Spearman"
        description = "If wall > enemy wall do 3 damage else do 2 damage"
        prop = 'wall'
        damage = -3 if players[0].kwargs['wall'] > players[1].kwargs['wall'] else -2
        self.damage(players[1], prop, damage)
        cost = {"gems": 10}
        # Call the constructor of the parent class with preset values
        super().__init__(title, description, cost)


class Dragon(Card):
    def __init__(self, players):
        title = "Dragon"
        description = "20 Damage. Enemy loses 10 gems, -1 enemy dungeon"
        prop = 'wall'
        damage = -20
        res = {'gems': -10, 'dungeon': -1}
        self.damage(players[1], prop, damage)
        self.resource(players[1], res)
        cost = {"recruits": 25}

        super().__init__(title, description, cost)


class Crystallize(Card):
    def __init__(self, players):
        title = 'Crystallize'
        description = "+11 Tower. -6 wall"
        res = {'tower': 11}
        self.resource(players[0], res)
        damage = min(6, players[0].kwargs['wall'])
        cost = {'gems': 8}
        self.damage(players[0], 'wall', -damage)

        super().__init__(title, description, cost)


class Tremors(Card):
    def __init__(self, players):
        title = 'Tremors'
        description = 'All walls take 5 damage. Play again'
        cost = {'bricks': 1000}
        damage = min(5, players[0].kwargs['wall'])
        self.damage(players[0], 'wall', -damage)
        damage = min(5, players[1].kwargs['wall'])
        self.damage(players[1], 'wall', -damage)
        super().__init__(title, description, cost)


class LavaJewel(Card):
    cost = {'gems': 17}

    def __init__(self, players):
        title = 'Lava Jewel'
        description = '+12 Tower, 6 Damage to enemy'

        res = {'tower': 12}
        self.resource(players[0], res)
        prop = 'wall'
        damage = -6
        self.damage(players[1], prop, damage)
        super().__init__(title, description)


class Spizzer(Card):
    cost = {'recruits': 8}

    def __init__(self, players):

        title = 'Spizzer'
        description = 'If enemy wall = 0, 10 damage, else 6 damage'
        prop = 'wall'
        damage = 10 if players[1].kwargs['wall'] == 0 else 6
        self.damage(players[1], prop, damage)

        super().__init__(title, description)