try:
    f = open("myWriteLines.txt", "w")
    lines = ["New line 1\n", "New line 2\n", "New line 3"]
    f.writelines(lines)
except:
    print("Something Wrong!!!")

print("Done!!!")
