# Create a dictionary with list of zipped keys/values
keys = ["name", "age", "job"]
values = ["Bob", 25, "Dev"]
print("Keys : ", keys)
print("Values : ", values)

D = dict(zip(keys, values))
print("The dictionary : ", D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
