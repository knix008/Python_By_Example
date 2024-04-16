try:
    f = open("myWrite.txt", "r+")
    f.write("---Overwrite content---")
except:
    print("Something Wrong!!!")

print("Done!!!")
