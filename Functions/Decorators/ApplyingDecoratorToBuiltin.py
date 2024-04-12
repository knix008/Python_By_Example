from functools import wraps


def double_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


double_the_sum = double_it(sum)

print(double_the_sum([1, 2]))
# Prints 6
