# Break the while loop when x becomes 3
x = 6

while x:
    print(x)
    x -= 1
    if x == 3:
        break
else:
    print("Done!")
# Prints 6 5 4
