A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
print('The Set A : ', A)
print('The Set B : ', B)

# by operator
print('A ^ B :', A ^ B)
# Prints {'orange', 'blue', 'green', 'yellow'}

# by method
print('A.symmetric_difference(B) :', A.symmetric_difference(B))
# Prints {'orange', 'blue', 'green', 'yellow'}