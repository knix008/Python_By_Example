try:
    # Open a file for reading
    f = open("myFile.csv")

    # Open a file for writing
    f = open("myFile.csv", "w")

    # Open a file for reading and writing
    f = open("myFile.csv", "r+")
except:
    print("Something Wrong!!!")

print("Done!!!")
