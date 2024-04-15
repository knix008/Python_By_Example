# Create and raise Custom exception 'InputError'
class InputError(Exception):
    pass

raise InputError('Custom exception')

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# InputError: Custom exception