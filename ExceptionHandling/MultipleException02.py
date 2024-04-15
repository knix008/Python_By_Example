# Execute same block of code for multiple exceptions
try:
    x = 1/0
except (ZeroDivisionError, ValueError):
    print('ZeroDivisionError or ValueError is raised')
except:
    print('Something else went wrong')
# Prints ZeroDivisionError or ValueError is raised