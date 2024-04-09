# A lambda function that returns the smallest item
findMin = lambda x, y: x if x < y else y

print(findMin(2, 4))
# Prints 2

print(findMin("a", "x"))
# Prints a
