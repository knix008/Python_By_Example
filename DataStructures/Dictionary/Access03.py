D = {"name": "Bob", "age": 25, "job": "Dev"}
print(D)

# When key is present
print(D.get("name"))
# Prints Bob

# When key is absent
print(D.get("salary"))
# Prints None
