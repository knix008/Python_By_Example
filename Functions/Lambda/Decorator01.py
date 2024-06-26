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


# Applying decorator to hello()
@debug
def hello(name):
    return "Hello " + name


# Calling the decorated function
print(hello("Bob"))
# Prints [DEBUG] Calling hello with argument ('Bob',) | Result: Hello Bob
# Prints Hello Bob
