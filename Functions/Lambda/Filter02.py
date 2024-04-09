# Filter the values above 18
age = [5, 11, 16, 19, 24, 42]
print("The Original List : ", age)
adults = filter(lambda x: x > 18, age)
print("The Modified List : ", list(adults))
# Prints [19, 24, 42]
