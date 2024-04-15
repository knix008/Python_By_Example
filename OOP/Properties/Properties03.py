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

    # make a property
    name = property(get_name, set_name)


p = Person("Bob")
print("The Name : ", p.name)
p.name = "Sam"
# Prints Setting name to Sam

print(p.name)
# Prints Getting name: Sam
