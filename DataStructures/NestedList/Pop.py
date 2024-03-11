L = ["a", ["bb", "cc", "dd"], "e"]
print(L)
x = L[1].pop(1)
print(L)
# Prints ['a', ['bb', 'dd'], 'e']

# removed item
print(x)
# Prints cc
