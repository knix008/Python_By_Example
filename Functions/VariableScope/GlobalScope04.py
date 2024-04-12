x = 42  # global scope x
print("The Original Value : ", x)


def myfunc():
    global x  # declare x global
    x = 0
    print(x)  # global x is now 0


myfunc()
print(x)  # x is 0
