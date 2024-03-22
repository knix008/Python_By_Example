# Create a dictionary with a list of two-item tuples
L = [("name", "Bob"), ("age", 25), ("job", "Dev")]
print(L)

D = dict(L)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Create a dictionary with a tuple of two-item lists
T = (["name", "Bob"], ["age", 25], ["job", "Dev"])
print(T)

D = dict(T)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
