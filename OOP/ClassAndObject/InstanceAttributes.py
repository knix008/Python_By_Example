# A class with two instance attributes
class Car:

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

car = Car("white", "SUV")
print("THe Attributes : ", car.color, car.style)