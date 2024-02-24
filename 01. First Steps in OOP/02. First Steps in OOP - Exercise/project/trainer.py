from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for poke in self.pokemons:
            if poke.name == pokemon_name:
                self.pokemons.pop(self.pokemons.index(poke))
                return f"You have released {pokemon_name}"

        return f"Pokemon is not caught"

    def trainer_data(self):
        data = [f"Pokemon Trainer {self.name}", f'Pokemon count {len(self.pokemons)}']
        for poke in self.pokemons:
            data.append(f'- {poke.pokemon_details()}')

        return '\n'.join(data)

