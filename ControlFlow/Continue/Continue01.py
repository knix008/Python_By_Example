# skip 'blue' while iterating a list
colors = ["red", "green", "blue", "yellow"]
print("The List : ", colors)

for x in colors:
    if x == "blue":
        continue
    print(x)
# Prints red green yellow
