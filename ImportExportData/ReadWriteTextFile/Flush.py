try:
    # Flush output buffer to disk without closing
    f = open("myFlush.txt", "a")
    f.write("Append this text.")
    f.flush()
except:
    print("Something Wrong!!!")

print("Done!!!")
