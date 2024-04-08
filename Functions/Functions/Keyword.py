# Keyword arguments can be put in any order
def func(name, job):
    print(name, "is a", job)


func(name="Bob", job="developer")
# Prints Bob is a developer

func(job="developer", name="Bob")
# Prints Bob is a developer
