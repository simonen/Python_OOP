from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for playa in self.players:
            if playa.name == player_name:
                playa.guild = 'Unaffiliated'
                self.players.remove(playa)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + '\n'.join([playa.player_info() for playa in self.players])

