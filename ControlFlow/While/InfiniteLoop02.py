# Loop runs until the user enters 'stop'
while True:
    name = input("Enter name:")
    if name == "stop":
        break
    print("Hello", name)

# Output:
# Enter name:Bob
# Hello Bob
# Enter name:Sam
# Hello Sam
# Enter name:stop
