D1 = {"emp1": {"name": "Bob", "job": "Mgr"}, "emp2": {"name": "Kim", "job": "Dev"}}

D2 = {"emp2": {"name": "Sam", "job": "Dev"}, "emp3": {"name": "Max", "job": "Janitor"}}

D1.update(D2)

print(D1)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Sam', 'job': 'Dev'},
#         'emp3': {'name': 'Max', 'job': 'Janitor'}}
