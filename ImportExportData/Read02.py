f = open("myTest.txt")

print(f.read(3))
# Prints Fir

# Go to offset 0
f.seek(0)
print(f.read(5))
# Prints First
