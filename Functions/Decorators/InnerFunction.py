def outer_func():
    print("Running outer")

    def inner_func():
        print("Running inner")

    inner_func()


outer_func()
# Prints Running inner
