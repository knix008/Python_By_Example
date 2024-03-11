# Insert at the start
L = ["a", "b", "c"]
print(L)
L[:0] = [1, 2, 3]
print(L)
# Prints [1, 2, 3, 'a', 'b', 'c']

# Insert at the end
L = ["a", "b", "c"]
print(L)
L[len(L) :] = [1, 2, 3]
print(L)
# Prints ['a', 'b', 'c', 1, 2, 3]
