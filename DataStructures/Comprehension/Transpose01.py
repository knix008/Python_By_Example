matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

L = [[row[i] for row in matrix] for i in range(3)]
print(L)
# Prints [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
