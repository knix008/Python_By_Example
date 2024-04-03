# Skip odd numbers
x = 6

while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x)
# Prints 4 2 0
