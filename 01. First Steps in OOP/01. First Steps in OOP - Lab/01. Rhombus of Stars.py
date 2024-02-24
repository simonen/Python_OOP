def print_stars(size, star_count):
    print(void * (size - star_count), end='')
    print(*[symbol] * star_count)


def top_triangle(size):
    for star_count in range(1, size):
        print_stars(size, star_count)


def reversed_triangle(size):
    for star_count in range(size, 0, -1):
        print_stars(size, star_count)


def rhombus(size):
    top_triangle(size)
    reversed_triangle(size)


n = int(input())
symbol = '*'
void = ' '
rhombus(n)
