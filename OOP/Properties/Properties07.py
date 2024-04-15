class Person:
    def __init__(self, value):
        self.hidden_name = value

    @property
    def name(self):
        print("Getting name:")
        return self.hidden_name

    @name.setter
    def name(self, value):
        print("Setting name to", value)
        self.hidden_name = value

    @name.deleter
    def name(self):
        print("Deleting name")
        del self.hidden_name


p = Person("Bob")

# calls the getter
print(p.name)
# Prints Getting name: Bob

# calls the setter
p.name = "Sam"
# Prints Setting name to Sam

# calls the deleter
del p.name
# Prints Deleting name
