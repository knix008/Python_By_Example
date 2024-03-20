# With list comprehension
L = [x for x in range(10) if x % 2 == 0]
print(L)
# Prints [0, 2, 4, 6, 8]

# With filter() function
L = list(filter((lambda x: x % 2 == 0), range(10)))
print(L)
# Prints [0, 2, 4, 6, 8]
