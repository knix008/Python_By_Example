colors = ["red", "green", "blue"]
print("The List : ", colors)

for x in colors[:]:
    if x == "red":
        colors.insert(0, "orange")
print(colors)
# Prints ['orange', 'red', 'green', 'blue']
