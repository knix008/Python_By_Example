def fibonacci(x):
    if x == 0 or x == 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)


# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))
# print(fibonacci(8))
# print(fibonacci(9))
print(fibonacci(10))
