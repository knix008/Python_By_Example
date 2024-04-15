class Person:
    def __init__(self, value):
        self.name = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


p = Person(42)  # Triggers TypeError: Expected a string
p = Person("Bob")
print(p.name)  # Prints Bob
p.name = 42  # Triggers TypeError: Expected a string
del p.name  # Triggers AttributeError: Can't delete attribute
