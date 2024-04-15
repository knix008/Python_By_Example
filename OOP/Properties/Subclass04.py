from Subclass03 import SubPerson

s = SubPerson("Bob")

# calls the getter
print(s.name)
# Prints Inside subperson getter
# Prints Getting name: Bob

# calls the setter
s.name = "Sam"
# Prints Inside subperson setter
# Prints Setting name to Sam

# calls the deleter
del s.name
# Prints Inside subperson deleter
# Prints Deleting name
