# Break the loop at 'blue'
colors = ["red", "green", "blue", "yellow"]
print("The list : ", colors)

for x in colors:
    if x == "blue":
        break
    print(x)
# Prints red green
