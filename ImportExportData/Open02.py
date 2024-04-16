try:
    # Open a file for reading
    f = open("myFile.txt")

    # Open a file for writing
    f = open("myFile.txt", "w")

    # Open a file for reading and writing
    f = open("myFile.txt", "r+")

    # Open a binary file for reading
    f = open("myFile.txt", "rb")
except:
    print("Something Wrong!!!")

print("Done!!!")
