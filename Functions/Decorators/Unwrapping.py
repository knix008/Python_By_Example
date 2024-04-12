from functools import wraps


def decorate_it(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@decorate_it
def hello():
    print("Hello world")


original_hello = hello.__wrapped__

original_hello()
# Prints Hello world
