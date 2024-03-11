L = ["a", ["bb", "cc"], "d"]
print(L)
L[1].extend([1, 2, 3])
print(L)
# Prints ['a', ['bb', 'cc', 1, 2, 3], 'd']
