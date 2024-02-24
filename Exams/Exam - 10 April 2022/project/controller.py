from project.player import Player
from project.supply.supply import Supply
from typing import List


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players) -> str:
        added_players = []
        for player in players:
            if player not in self.players:
                added_players.append(player)
                self.players.append(player)

        return f"Successfully added: {', '.join(x.name for x in added_players)}"

    def add_supply(self, *supplies) -> None:
        for item in supplies:
            self.supplies.append(item)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next((p for p in self.players if p.name == player_name), None)
        if not player or sustenance_type not in ['Food', 'Drink']:
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        item = next((i for i in self.supplies[::-1] if i.__class__.__name__ == sustenance_type), None)
        if not item:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + item.energy, 100)

        index = self.supplies[::-1].index(item)
        self.supplies.pop(-index - 1)

        return f"{player_name} sustained successfully with {item.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        first_player = next(fp for fp in self.players if fp.name == first_player_name)
        second_player = next(sp for sp in self.players if sp.name == second_player_name)

        no_stamina = [f"Player {p.name} does not have enough stamina."
                      for p in [first_player, second_player] if p.stamina == 0]
        if no_stamina:
            return '\n'.join(no_stamina)

        players = sorted([first_player, second_player], key=lambda x: x.stamina)
        for _ in range(2):
            if players[1].stamina - (players[0].stamina / 2) <= 0:
                players[1].stamina = 0
                break

            players[1].stamina -= (players[0].stamina / 2)
            players[0], players[1] = players[1], players[0]

        return f"Winner: {max(players, key=lambda x: x.stamina).name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), 0)

            for food_type in ['Food', 'Drink']:
                item = next((i for i in self.supplies[::-1] if i.__class__.__name__ == food_type), None)
                if not item:
                    continue

                player.stamina = min(player.stamina + item.energy, 100)

                index = self.supplies[::-1].index(item)
                self.supplies.pop(-index - 1)

    def __str__(self):
        players = [str(p) for p in self.players]
        supply = [s.details() for s in self.supplies]
        players.extend(supply)
        return "\n".join(players)
