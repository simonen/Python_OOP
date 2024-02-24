class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = 0
        self.end = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            i = self.end
            self.end -= 1
            return self.iterable[i]
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, False, 11, True])
for item in reversed_list:
    print(item)
