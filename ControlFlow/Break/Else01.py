# Break the for loop at 'blue'
colors = ["red", "green", "blue", "yellow"]
print("The List : ", colors)

for x in colors:
    if x == "blue":
        break
    print(x)
else:
    print("Done!")
# Prints red green
