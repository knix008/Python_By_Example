# base class
class Vehicle:
    def description(self):
        print("I'm a Vehicle!")


# subclass
class Car(Vehicle):
    pass


c = Car()
c.description()
