# a parent class
class Vehicle():
    def description(self):
        print("I'm a", self.color, "Vehicle")

# subclass
class Car(Vehicle):
    def description(self):
        print("I'm a", self.color, self.style)
    def setSpeed(self, speed):
        print("Now traveling at", speed,"miles per hour")    

# create an object from each class
v = Vehicle()
c = Car()

c.setSpeed(25)
# Prints Now traveling at 25 miles per hour
v.setSpeed(25)
# Triggers AttributeError: 'Vehicle' object has no attribute 'setSpeed'