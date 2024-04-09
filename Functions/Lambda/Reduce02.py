from functools import reduce

L = [10, 20, 30, 40]
print("The Original List : ", L)
result = reduce(lambda a, b: a + b, L)
print("The Modified List : ", result)
# Prints 100
