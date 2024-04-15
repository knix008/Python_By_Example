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


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print("Inside subperson getter")
        return super().name

    @Person.name.setter
    def name(self, value):
        print("Inside subperson setter")
        super(SubPerson, SubPerson).name.__set__(self, value)

    @Person.name.deleter
    def name(self):
        print("Inside subperson deleter")
        super(SubPerson, SubPerson).name.__delete__(self)
