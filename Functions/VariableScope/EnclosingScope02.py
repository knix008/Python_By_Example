# enclosing function
def f1():
    x = 42

    # nested function
    def f2():
        nonlocal x
        x = 0
        print("The Nested X : ", x)  # x is now 0

    f2()
    print(x)  # x remains 0


f1()
