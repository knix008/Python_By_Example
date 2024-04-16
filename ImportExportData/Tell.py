f = open("alphaText.txt")

# initial position
print(f.tell())
# Prints 0

# after reading 5 characters
f.read(5)
print(f.tell())
# Prints 5
