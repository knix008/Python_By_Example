def decorate_it(func):
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
# Prints wrapper
print(hello.__doc__)
# Prints None
print(hello)
# Prints <function decorate_it.<locals>.wrapper at 0x02E15078>
