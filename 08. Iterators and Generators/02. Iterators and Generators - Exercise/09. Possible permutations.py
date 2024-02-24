from itertools import permutations


def possible_permutations(args: list):
    for i in permutations(args):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
