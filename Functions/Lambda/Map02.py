# Double each item of the list
L = [1, 2, 3, 4, 5, 6]
print("The Original List : ", L)
doubler = map(lambda x: x * 2, L)
print(doubler)
print("The Modified List : ", list(doubler))
# Prints [2, 4, 6, 8, 10, 12]
