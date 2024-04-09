def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)


result = outer(2, 4)
print(result)
# Prints 6

# You cannot use the nested function out of the function.
# result = inner(3, 5)
# print(result)
