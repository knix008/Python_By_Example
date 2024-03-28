D = {
    "emp1": {"name": "Bob", "job": "Mgr"},
    "emp2": {"name": "Kim", "job": "Dev"},
    "emp3": {"name": "Sam", "job": "Dev"},
}

# key present
print(D["emp1"].get("name"))
# Prints Bob

# key absent
print(D["emp1"].get("salary"))
# PrintsNone
