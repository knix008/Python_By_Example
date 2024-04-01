D = {(k, v): k + v for k in range(2) for v in range(2)}
print(D)
# Prints {(0, 1): 1, (1, 0): 1, (0, 0): 0, (1, 1): 2}

# is equivalent to
D = {}
for k in range(2):
    for v in range(2):
        D[(k, v)] = k + v
print(D)
# Prints {(0, 1): 1, (1, 0): 1, (0, 0): 0, (1, 1): 2}
