# With list comprehension
L = [x**2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]

# With map() function
L = list(map((lambda x: x**2), range(5)))
print(L)
# Prints [0, 1, 4, 9, 16]
