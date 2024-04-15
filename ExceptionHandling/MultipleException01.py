# Print one message for ZeroDivisionError and another for all other errors
try:
	x = 1/0
except ZeroDivisionError:
	print('Attempt to divide by zero')
except:
	print('Something else went wrong')
# Prints Attempt to divide by zero