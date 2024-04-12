x = 42  # global scope x
print("The Original Value : ", x)


def myfunc():
    x = x + 1  # raises UnboundLocalError
    print(x)


myfunc()
