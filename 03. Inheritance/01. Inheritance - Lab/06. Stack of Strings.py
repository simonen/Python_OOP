from typing import List


class BaseStack:

    def __init__(self):
        self.data: List[str] = []

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'


class AddStack(BaseStack):

    def push(self, element: str):
        self.data.append(element)


class PopStack(BaseStack):

    def pop(self):
        return self.data.pop() if len(self.data) > 0 else self.data


class TopStack(BaseStack):

    def top(self):
        return self.data[-1]


class Stack(AddStack, PopStack, TopStack):
    pass


stack = Stack()
print(stack.is_empty())
print(stack)
stack.push("apple")
stack.push("carrot")
print(stack)
stack.pop()

print(stack)
print(stack.is_empty())

