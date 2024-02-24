from math import sqrt


def get_primes(integers: list):
    for i in integers:
        if i < 2:
            continue
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            yield i


print(list(get_primes([100_000_007, 4, 3, 5, 6, 9, 1, 0])))
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))
#
# inter = [-2, 0, 0, 1, 1, 0]

