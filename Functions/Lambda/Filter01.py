# Filter the values above 18
def checkAge(age):
    if age > 18:
        return True
    else:
        return False


age = [5, 11, 16, 19, 24, 42]
print("The Original List : ", age)
adults = filter(checkAge, age)
print("The Modified List : ", list(adults))
# Prints [19, 24, 42]
