class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.iterations = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == 0:
            raise StopIteration

        self.iterations -= 1

        return self.iterations


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
