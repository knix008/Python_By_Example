try:
    f = open("myAppend.txt", "a")
    f.write(" Append this text.")
except:
    print("Something Wrong!!!")

print("Done!!!")
