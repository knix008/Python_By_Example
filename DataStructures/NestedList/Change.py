L = ["a", ["bb", "cc"], "d"]
print(L)
L[1][1] = 0
print("The changed L : ", L)
# Prints ['a', ['bb', 0], 'd']
