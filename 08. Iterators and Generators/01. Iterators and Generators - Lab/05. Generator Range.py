def genrange(start: int, end: int) -> list:
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 22)))
