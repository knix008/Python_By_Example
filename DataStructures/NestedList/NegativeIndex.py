L = ["a", "b", ["cc", "dd", ["eee", "fff"]], "g", "h"]
print(L)

print("The item in L[-3] : ", L[-3])
# Prints ['cc', 'dd', ['eee', 'fff']]

print("The item in L[-3][-1] : ", L[-3][-1])
# Prints ['eee', 'fff']

print("The item in L[-3][-1][-2] : ", L[-3][-1][-2])
# Prints eee
