import os

try:
    f = open("myTemp.txt", "x")
except:
    print("Something Wrong in Open!!!")


try:
    os.remove("myTemp.txt")
except:
    print("Something Wrong in Remove!!!")


print("Done!!!")
