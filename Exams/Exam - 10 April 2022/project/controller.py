from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply
from typing import List


class Controller:
    SUPPLY_TYPES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players):
        new_players = [x for x in players if x not in self.players]
        self.players.extend(new_players)

        return f"Successfully added: {', '.join(x.name for x in new_players)}"

    def add_supply(self, *supplies) -> None:
        self.supplies += [x for x in supplies]

    def _get_player(self, player_name: str) -> Player | None:
        player = next((x for x in self.players if x.name == player_name), None)
        return player

    def _get_supply_item(self, sustenance_type: str) -> Supply | None:
        item_index = next((i for i in range(len(self.supplies) -1, -1, -1)
                                  if isinstance(self.supplies[i], type(self).SUPPLY_TYPES[sustenance_type])), None)
        if item_index is not None:
            item = self.supplies.pop(item_index)
            return item
        return None

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._get_player(player_name)
        if player is None:
            return None

        if sustenance_type not in Controller.SUPPLY_TYPES:
            return None

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        last_added_supply = self._get_supply_item(sustenance_type)
        if last_added_supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + last_added_supply.energy, 100)

        return f"{player_name} sustained successfully with {last_added_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        first_player = self._get_player(first_player_name)
        second_player = self._get_player(second_player_name)
        no_stamina = [x.name for x in (first_player, second_player) if x.stamina == 0]
        if no_stamina:
            res = [f"Player {player} does not have enough stamina." for player in no_stamina]
            return "\n".join(res)

        belligerents = sorted((first_player, second_player), key=lambda x: x.stamina)
        attacker, defender = belligerents[0], belligerents[1]

        for _ in range(2):
            defender.stamina = min(defender.stamina - (attacker.stamina / 2), 0)
            if defender.stamina == 0:
                break

            attacker, defender = belligerents[1], belligerents[0]

        winner = max((attacker, defender), key=lambda x: x.stamina)
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), 0)

            food = self._get_supply_item("Food")
            drink = self._get_supply_item("Drink")

            if food is not None:
                player.stamina = min(player.stamina + food.energy, 100)
            if drink is not None:
                player.stamina = min(player.stamina + drink.energy, 100)

    def __str__(self):
        res = [str(x) for x in self.players] + [x.details() for x in self.supplies]
        return "\n".join(res)

