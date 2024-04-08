# in a while statement
while 1:
    try:
        print("trying...")
        break
        print("still trying...")
    except:
        print("Something went wrong.")
    finally:
        print("Done!")
# Prints trying...
# Prints Done!
