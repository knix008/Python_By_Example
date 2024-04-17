try:
    # Create a file and open it for writing
    # write mode
    f = open("newFile.txt", "w")

    # append mode
    f = open("newFile.txt", "a")

    # read + write mode
    f = open("newFile.txt", "r+")
except:
    print("Something Wrong!!!")

print("Done!!!")
