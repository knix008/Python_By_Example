D = {
    "emp1": {"name": "Bob", "job": "Mgr"},
    "emp2": {"name": "Kim", "job": "Dev"},
    "emp3": {"name": "Sam", "job": "Dev"},
}

print(D["emp1"]["name"])
# Prints Bob

print(D["emp2"]["job"])
# Prints Dev

print(D["emp1"]["salary"])
# Triggers KeyError: 'salary'
