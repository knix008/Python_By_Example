# Flatten a nested list with lambda
flatten = lambda l: [item for sublist in l for item in sublist]

L = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print(flatten(L))
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

L = [["a", "b", "c"], ["d", "e"]]
print(flatten(L))
# Prints ['a', 'b', 'c', 'd', 'e']
