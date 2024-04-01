D = {0: "red", 1: "green", 2: "blue"}
print(D)

R = {v: k for k, v in D.items()}
print("Reverse : ", R)
# Prints {'red': 0, 'green': 1, 'blue': 2}
