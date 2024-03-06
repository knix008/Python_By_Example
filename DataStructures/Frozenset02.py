# finding size
S = frozenset({'red', 'green', 'blue'})
print(len(S))
# Prints 3

# performing union
S = frozenset({'red', 'green', 'blue'})
print(S | {'yellow'})
# Prints frozenset({'blue', 'green', 'yellow', 'red'})