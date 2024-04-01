keys = ["name", "age", "job"]
values = ["Bob", 25, "Dev"]
print("Keys : ", keys)
print("Values : ", values)

# using dict comprehension
D = {k: v for (k, v) in zip(keys, values)}
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# equivalent to using dict() on zipped keys/values
D = dict(zip(keys, values))
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
