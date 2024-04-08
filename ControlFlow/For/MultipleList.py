# Loop through two lists at once
name = ["Bob", "Sam", "Max"]
age = [25, 35, 30]
print("The List name : ", name)
print("The List age : ", age)

for x, y in zip(name, age):
    print(x, y)
# Prints Bob 25
# Prints Sam 35
# Prints Max 30
