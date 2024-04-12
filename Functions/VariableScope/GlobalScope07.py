x = 42  # global scope x
print("The Original Value : ", x)


def myfunc():
    globals()["x"] = globals()["x"] + 1  # raises UnboundLocalError
    print(globals()["x"])


myfunc()
