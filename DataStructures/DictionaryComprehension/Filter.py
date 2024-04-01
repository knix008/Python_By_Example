D = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
print(D)
removeKeys = [0, 2, 5]

X = {k: D[k] for k in D.keys() - removeKeys}

print(X)
# Prints {1: 'B', 3: 'D', 4: 'E'}
