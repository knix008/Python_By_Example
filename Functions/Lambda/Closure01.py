def multiplier(x):
    def inner_func(y):
        return x * y

    return inner_func


doubler = multiplier(2)
print(doubler(10))
# Prints 20

tripler = multiplier(3)
print(tripler(10))
# Prints 30
