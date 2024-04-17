try:
    f = open("myWrite.txt", "w")
    f.write("Overwrite existing data.")
except:
    print("Something Wrong!!!")

print("Done!!!")
