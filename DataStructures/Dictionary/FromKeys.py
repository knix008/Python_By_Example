# Initialize dictionary with default value '0' for each key
keys = ["a", "b", "c"]
defaultValue = 0
print("Keys : ", keys)

D = dict.fromkeys(keys, defaultValue)

print(D)
# Prints {'a': 0, 'b': 0, 'c': 0}
