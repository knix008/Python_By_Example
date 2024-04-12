def decorate_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@decorate_it
def hello(name):
    print("Hello", name)


hello("Bob")
# Prints _wrapper() takes 0 positional arguments but 1 was given
