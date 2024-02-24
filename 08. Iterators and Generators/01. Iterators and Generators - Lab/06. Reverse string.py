def reverse_text(string: str):
    start = len(string) - 1
    end = 0
    i = start
    while i >= end:
        yield string[i]
        i -= 1


for char in reverse_text("step"):
 print(char, end='')