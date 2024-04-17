try:
    # Create a file exclusively
    f = open("newFile.txt", "x")
except:
    print("Something Wrong!!!")

print("Done!!!")
