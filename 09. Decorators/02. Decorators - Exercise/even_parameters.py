def even_parameters(func):
    def wrapper(*args):
        if any(x for x in args if not isinstance(x, int | float) or x % 2 != 0):
            return "Please use only even numbers!"
        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add(2, 'AZ'))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

# Fun stuff
print(True + False)   # 1    # True = 1, False = 0
print(sum([True, True])) # 1 Count how many conditions are true
print(isinstance(True, int))   # True
print(True == 1)  # True