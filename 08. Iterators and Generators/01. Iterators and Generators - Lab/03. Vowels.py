class vowels:

    def __init__(self, string: str):
        self.string = string
        self.vowels = list('aeiouy')
        self.i = 0
        self.end = len(self.string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            i = self.i
            self.i += 1
            if self.string[i].lower() in self.vowels:
                return self.string[i]
            return self.__next__()
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
 print(char)