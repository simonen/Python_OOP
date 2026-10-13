def logged(f):
    def wrapper(*args):
        return (f"you called {f.__name__}{args}\n"
                f"it returned {f(*args)}")
    return wrapper


@logged
def func(*args):
    return 3 + len(args)

@logged
def sum_func(a, b):
    return a + b

print(func(1, 2, False, True, None, "stako"))
print(sum_func(1, 4))