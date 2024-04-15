# finally clause is always executed
try:
	x = 1/0
except:
	print('Something went wrong')
finally:
	print('Always execute this')
# Prints Something went wrong
# Prints Always execute this