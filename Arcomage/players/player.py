
class Player:
    def __init__(self, name: str, **kwargs):

        self.name = name
        self.kwargs = kwargs
        self.deck = []

    # def __repr__(self):
    #     # res = {k: v for k, v in self.kwargs}
    #     res = self.kwargs
    #     # res = [f"{k ,v}" for k, v in self.kwargs.items()]
    #     # res.insert(0, self.name)
    #     return res
