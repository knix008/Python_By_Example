import os

if os.path.isfile("myFile.txt"):
    f = open("myFile.txt")
    print("Success!!!")
else:
    print("The file does not exist.")
