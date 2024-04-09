multiplier = lambda x: (lambda y: x * y)

doubler = multiplier(2)
print(doubler(10))
# Prints 20

tripler = multiplier(3)
print(tripler(10))
# Prints 30
