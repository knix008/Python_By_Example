# Unpack returned tuple
def func(a, b):
    return a + b, a - b


add, sub = func(3, 2)
print(add)
# Prints 5
print(sub)
# Prints 1
