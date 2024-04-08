# Flatten a nested list
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("The List : ", list)

for sublist in list:
    for number in sublist:
        print(number)
# Prints 1 2 3 4 5 6 7 8 9
