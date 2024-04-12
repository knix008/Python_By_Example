from functools import wraps


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return wrapper


sum = debug(sum)
sum([1, 2, 3])
# Prints Running function: sum
# Prints Positional arguments: ([1, 2, 3],)
# Prints keyword arguments: {}
# Prints Result: 6
