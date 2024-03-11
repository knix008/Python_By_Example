L = ["a", ["bb", "cc"], "d"]
print(L)
L[1].insert(0, "xx")
print(L)
# Prints ['a', ['xx', 'bb', 'cc'], 'd']
