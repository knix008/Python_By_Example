# Double each item of the list
def doubler(x):
    return x * 2


L = [1, 2, 3, 4, 5, 6]
print("The Original List : ", L)
mod_list = map(doubler, L)
print("The Modified List : ", list(mod_list))
# Prints [2, 4, 6, 8, 10, 12]
