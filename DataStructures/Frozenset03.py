# removing an item
#S = frozenset({'red', 'green', 'blue'})
#S.pop()
# Triggers AttributeError: 'frozenset' object has no attribute 'pop'

# adding an item
S = frozenset({'red', 'green', 'blue'})
S.add('yellow')
# Triggers AttributeError: 'frozenset' object has no attribute 'add'