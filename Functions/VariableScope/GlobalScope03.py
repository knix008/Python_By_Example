x = 42  # global scope x
print("The Original Value : ", x)


def myfunc():
    x = 0
    print(x)  # local x is 0


myfunc()
print(x)  # global x is still 42
