# Remove whitespaces of list items
colors = ["  red", "  green ", "blue  "]
print(colors)

L = [color.strip() for color in colors]
print(L)
# Prints ['red', 'green', 'blue']
