# Filter list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
print(vec)

L = [x for x in vec if x >= 0]
print(L)
# Prints [0, 2, 4]
