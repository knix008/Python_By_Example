x = 42  # global scope x


def myfunc():
    print(x)  # x is 42 inside def


myfunc()
print(x)  # x is 42 outside def
