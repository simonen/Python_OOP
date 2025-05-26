import random
from typing import List
from cards.card import *
from players.player import Player

# class Deck:
#     def __init__(self):
#         titles = ['Foundations', 'Dragon', 'Lightning Shard', 'New Equipment']
#         description = ["If wall = 0, +6 wall, else +3 wall",
#                        "20 Damage. Enemy loses 10 gems, -1 enemy dungeon",
#                        "If Tower > enemy wall, 8 damage to enemy tower. Else 8 damage",
#                        "+2 Quarry"]
#         own = [{"wall": 6} if player1.wall == 0 else {"wall": 3}]
#         self.cards = []


class Game:
    def __init__(self, name: str):
        self.name = name
        self.players: List = [Player]
        self.deck = [LavaJewel, Tremors, Crystallize, Dragon,
                     Spearman, PearlOfWisdom, LightningShard, StripMine, Foundations, NewEquipment, Succubus]

    def players_spawn(self) -> None:
        p1 = Player("Penka", tower=20, wall=3, quarry=5, magic=5, dungeon=5, bricks=20, gems=16, recruits=20)
        p2 = Player("Gliga", tower=20, wall=1, quarry=5, magic=5, dungeon=5, bricks=20, gems=20, recruits=20)
        self.players = [p1, p2]
        print(f'Adding players: {p1.name} and {p2.name}')

    def harvest(self) -> None:
        for i in range(2):
            self.players[i].kwargs['bricks'] += self.players[i].kwargs['quarry']
            self.players[i].kwargs['gems'] += self.players[i].kwargs['magic']
            self.players[i].kwargs['recruits'] += self.players[i].kwargs['dungeon']

    def draw_card(self, card_num: int):
        res = list(self.deck[card_num].cost.keys())[0]
        if self.players[0].kwargs[res] >= self.deck[card_num].cost[res]:
            card = self.deck[card_num](self.players)
            self.players[0].kwargs[res] -= self.deck[card_num].cost[res]
            return card.description
        return 'nqma pari'


game = Game("arco")
print(game.players_spawn())
# print('playa', game.players[0])

# game.harvest()
print(game.players[0].kwargs)
print(game.players[1].kwargs)
game.draw_card(0)
print(game.players[0].kwargs)
print(game.players[1].kwargs)