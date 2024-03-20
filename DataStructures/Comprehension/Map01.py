# With list comprehension
L = [ord(x) for x in "foo"]
print(L)
# Prints [102, 111, 111]

# With map() function
L = list(map(ord, "foo"))
print(L)
# Prints [102, 111, 111]
