# Return multiple values by packing them in a tuple
findSquareCube = lambda num: (num**2, num**3)
x, y = findSquareCube(2)
print(x)
# Prints 4
print(y)
# Prints 8
