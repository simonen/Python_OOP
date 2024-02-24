def start_playing(instrument):
    return instrument.play()


class Guitar:
    def play(self) -> str:
        return 'Playing the guitar'


class Children:
    def play(self) -> str:
        return "Children are playing"



print(start_playing(Guitar()))
children = Children()
print(start_playing(children))