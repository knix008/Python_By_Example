def decorate_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@decorate_it
def hello():
    print("Hello world")


hello()
# Prints Before function call
# Prints Hello world
# Prints After function call
