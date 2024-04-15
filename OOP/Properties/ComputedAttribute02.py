class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(2, 5)
print(r.area)
# Prints 10

r.width = 3
r.height = 6

print(r.area)
# Prints 18

r.area = 18  # Triggers AttributeError: can't set attribute
