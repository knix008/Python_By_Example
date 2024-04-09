# Set default value 'developer' to a 'job' parameter
def func(name, job="developer"):
    print(name, "is a", job)


func("Bob", "manager")
# Prints Bob is a manager

func("Bob")
# Prints Bob is a developer
