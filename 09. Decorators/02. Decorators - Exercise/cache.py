def cache(func):
    cached = {}
    def wrapper(n):
        print(f"Calling {func.__name__}")
        print(cached)
        if n not in cached:
            cached[n] = func(n)
        return cached[n]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(11))

# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# 55
# Calling fibonacci
# Calling fibonacci
# Calling fibonacci
# 89
