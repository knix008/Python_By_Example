from functools import wraps


# Defining a decorator
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        print(
            f"[DEBUG] Calling {func.__name__} with argument {args} | Result: {result}"
        )
        return result

    return wrapper


print(list(map(debug(lambda x: x * 2), range(3))))
# Prints [DEBUG] Calling <lambda> with argument (0,) | Result: 0
# Prints [DEBUG] Calling <lambda> with argument (1,) | Result: 2
# Prints [DEBUG] Calling <lambda> with argument (2,) | Result: 4
# Prints [0, 2, 4]
