D = {
    "emp1": {"name": "Bob", "job": "Mgr"},
    "emp2": {"name": "Kim", "job": "Dev"},
    "emp3": {"name": "Sam", "job": "Dev"},
}

D["emp3"]["name"] = "Max"
D["emp3"]["job"] = "Janitor"

print(D["emp3"])
# Prints {'name': 'Max', 'job': 'Janitor'}
