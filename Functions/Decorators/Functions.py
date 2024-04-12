def hello1():
    print("Hello World")


def hello2():
    print("Hello Universe")


def greet(func):
    func()


greet(hello1)
# Prints Hello World
greet(hello2)
# Prints Hello Universe
