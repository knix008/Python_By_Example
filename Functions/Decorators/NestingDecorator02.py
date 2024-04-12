from functools import wraps


def double_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


def square_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return wrapper


@square_it
@double_it
def add(x, y):
    return x + y


result = add(2, 3)
print(result)
