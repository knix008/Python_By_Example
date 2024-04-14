# A class with one class attribute
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style


car1 = Car("Blue", "Sedan")
car2 = Car("White", "SUV")
print("The Car1 Attributes : ", car1.wheels, car1.color, car1.style)
print("The Car2 Attributes : ", car2.wheels, car2.color, car2.style)