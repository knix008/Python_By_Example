D = {
    "emp1": {"name": "Bob", "job": "Mgr"},
    "emp2": {"name": "Kim", "job": "Dev"},
    "emp3": {"name": "Sam", "job": "Dev"},
}
print(D)

del D["emp3"]

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}
