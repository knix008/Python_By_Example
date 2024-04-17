f = open("alphaText.txt", "rb+")

# go to the 7th character and read one character
f.seek(6)
print(f.read(1))
# Prints G

# go to the 3rd character from current position (letter G)
f.seek(3, 1)
print(f.read(1))
# Prints K

# go to the 3rd character before the end
f.seek(-3, 2)
print(f.read(1))
# Prints X
