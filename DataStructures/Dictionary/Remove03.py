D = {"name": "Bob", "age": 25, "job": "Dev"}
print(D)

x = D.popitem()
print(D)
# Prints {'name': 'Bob', 'age': 25}

# get removed pair
print(x)
# Prints ('job', 'Dev')
