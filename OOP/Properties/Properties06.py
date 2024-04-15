class Person:
    def __init__(self, value):
        self.hidden_name = value

    # getter function
    def get_name(self):
        print("Getting name:")
        return self.hidden_name

    # setter function
    def set_name(self, value):
        print("Setting name to", value)
        self.hidden_name = value

    # deleter function
    def del_name(self):
        print("Deleting name")
        del self.hidden_name

    # make a property
    name = property(get_name, set_name, del_name, doc="name of the person")


p = Person("Bob")

# calls the getter
print(p.name)
# Prints Getting name: Bob

# calls the setter
p.name = "Sam"
# Prints Setting name to Sam

# docstring
print("Docstring:", Person.name.__doc__)
# Prints Docstring: name of the person

# docstring
print("Docstring:", p.name.__doc__)
# Prints Docstring: name of the person

# calls the deleter
del p.name
# Prints Deleting name
