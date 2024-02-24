class custom_range:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            i = self.start
            self.start += 1
            return i
        else:
            raise StopIteration()


cus_range = custom_range(1, 10)
for i in cus_range:
    print(i)