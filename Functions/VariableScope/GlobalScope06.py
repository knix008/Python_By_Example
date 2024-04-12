x = 42  # global scope x
print("The Original Value : ", x)


def myfunc():
    global x
    x = x + 1  # global x is now 43
    print(x)


myfunc()
print(x)  # x is 43
