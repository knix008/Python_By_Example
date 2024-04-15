def this_fails():
    x = 1/0

try:
    this_fails()
except Exception as e:
    print(e)
# Prints division by zero