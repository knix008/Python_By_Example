# in a for statement
for x in range(5):
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
