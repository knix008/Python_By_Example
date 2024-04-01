keys = ["red", "green", "blue"]
print("Keys : ", keys)

# using dict comprehension
D = {k: 0 for k in keys}
print(D)
# Prints {'red': 0, 'green': 0, 'blue': 0}

# equivalent to using fromkeys() method
D = dict.fromkeys(keys, 0)
print(D)
# Prints {'red': 0, 'green': 0, 'blue': 0}
