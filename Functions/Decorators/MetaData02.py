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
    """function that greets"""
    print("Hello world")


print(hello.__name__)
# Prints hello
print(hello.__doc__)
# Prints function that greets
print(hello)
# Prints <function hello at 0x02DC5BB8>
