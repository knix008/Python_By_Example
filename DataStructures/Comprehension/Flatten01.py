# With list comprehension
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Vector : ", vector)

L = [number for list in vector for number in list]
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# equivalent to the following plain, old nested loop:
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Vector : ", vector)

L = []
for list in vector:
    for number in list:
        L.append(number)
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
