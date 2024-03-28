IDs = ["emp1", "emp2", "emp3"]

EmpInfo = [
    {"name": "Bob", "job": "Mgr"},
    {"name": "Kim", "job": "Dev"},
    {"name": "Sam", "job": "Dev"},
]

D = dict(zip(IDs, EmpInfo))

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'}}
