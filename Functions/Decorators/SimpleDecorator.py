def decorate_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


def hello():
    print("Hello world")


hello = decorate_it(hello)

hello()
# Prints Before function call
# Prints Hello world
# Prints After function call
