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


# Calling the decorated function
print((debug(lambda x: x**2))(3))
# Prints [DEBUG] Calling <lambda> with argument (3,) | Result: 9
# Prints 9
