def close_file():
    with open("myFile.txt") as f:
        print(f.read())
    print("Done")


close_file()
