# base class
class Vehicle:
    def description(self):
        print("I'm a Vehicle!")


# subclass
class Car(Vehicle):
    def description(self):
        print("I'm a Car!")


# create an object from each class
v = Vehicle()
c = Car()

v.description()
c.description()
