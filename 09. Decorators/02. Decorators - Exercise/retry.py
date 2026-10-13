from functools import wraps


def retry(retries):
    print(retries, "retries on failure")
    def decorator(func):
        print("Decorating", func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 2):
                print("Calling", func.__name__)
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    if attempt <= retries:
                        print("Retrying...", attempt)
                    else:
                        print("Caught:", exc)
        return wrapper
    return decorator


@retry(retries=2)
def fonc(number: int):
    print(f"{number} + 1 = {number + 1}")

fonc(None)