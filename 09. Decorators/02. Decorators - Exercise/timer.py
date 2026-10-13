import time

class Timer:
    def __init__(self, unit: str = 's'):
        self.unit = unit
        self.factor = {'s': 1, 'ms': 1000, 'us': 1000_000}[unit]
        print("Decorating...")

    def __call__(self, func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            st = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.time()
            ent = time.perf_counter()
            print(f"{func.__name__}() took {end - start:.2f} seconds | {(end - start) * self.factor:.3f}")
            return result
        return wrapper

@Timer(unit='ms')
def shout():
    return "Let i all aout"

shout()