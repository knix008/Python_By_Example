# enclosing function
def f1():
    x = 42

    # nested function
    def f2():
        x = 0
        print("The Nested X : ", x)  # x is 0

    f2()
    print(x)  # x is still 42


f1()
