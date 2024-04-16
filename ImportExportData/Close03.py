f = open("myFile.txt")
try:
    # File operations goes here
    print("Operation...")
finally:
    print("Closing file")
    f.close()
