# Sort the list of taples by the age of students
L = [("Sam", 35), ("Max", 25), ("Bob", 30)]
print("The List : ", L)

x = sorted(L, key=lambda student: student[1])
print("The Sorted List : ", x)
# Prints [('Max', 25), ('Bob', 30), ('Sam', 35)]
