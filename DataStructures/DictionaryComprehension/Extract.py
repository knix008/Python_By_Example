D = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
print(D)
selectedKeys = [0, 2, 5]

X = {k: D[k] for k in selectedKeys}

print(X)
# Prints {0: 'A', 2: 'C', 5: 'F'}
