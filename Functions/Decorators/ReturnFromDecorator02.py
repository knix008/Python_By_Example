def decorate_it(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@decorate_it
def hello(name):
    return "Hello " + name


result = hello("Bob")

print(result)
# Prints Before function call
# Prints After function call
# Prints Hello Bob
