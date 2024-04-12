def myfunc():
    x = 42  # local scope x


myfunc()
print(x)  # Triggers NameError: x does not exist
