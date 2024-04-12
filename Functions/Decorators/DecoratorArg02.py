def decorate_it(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")

    return wrapper


@decorate_it
def hello(name):
    print("Hello", name)


hello("Bob")
# Prints Before function call
# Prints Hello Bob
# Prints After function call
