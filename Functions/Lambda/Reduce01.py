# sum all items in a list
from functools import reduce


def summary(a, b):
    return a + b


L = [10, 20, 30, 40]
print("The Original List : ", L)
result = reduce(summary, L)
print("The Modified List : ", result)
# Prints 100
