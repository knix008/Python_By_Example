f = open("myFile.csv")
try:
    # File operations goes here
    print(f.read())
finally:
    f.close()
