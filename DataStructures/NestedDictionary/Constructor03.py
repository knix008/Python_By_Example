IDs = ["emp1", "emp2", "emp3"]
Defaults = {"name": "", "job": ""}

D = dict.fromkeys(IDs, Defaults)

print(D)
# Prints {'emp1': {'name': '', 'job': ''},
#         'emp2': {'name': '', 'job': ''},
#         'emp3': {'name': '', 'job': ''}}
