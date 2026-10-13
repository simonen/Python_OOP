def bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"
    return wrapper

def underline(func):
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"
    return wrapper

@underline
@italic
@bold
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))