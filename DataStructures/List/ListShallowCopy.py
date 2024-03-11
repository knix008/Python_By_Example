print("---Assignment---")
L = ["red", "green", "yellow"]
print(L)

M = L
print(M)
M[0] = 1
M[1] = 2
M[2] = 3

print("New : ", M)
print("Old : ", L)
print("")

print("---Shallow Copy---")
L = ["red", "green", "yellow"]
print(L)

M = L.copy()
print(M)
M[0] = 1
M[1] = 2
M[2] = 3

print("New : ", M)
print("Old : ", L)
