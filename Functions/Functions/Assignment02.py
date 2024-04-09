def findSquare(x):
    return x**2


def findCube(x):
    return x**3


# Create a dictionary of functions
exponent = {"square": findSquare, "cube": findCube}

print(exponent["square"](3))
# Prints 9
print(exponent["cube"](3))
# Prints 27
