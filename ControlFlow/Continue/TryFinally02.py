# in a while statement
x = 2

while x:
    try:
        print("trying...")
        x -= 1
        continue
        print("still trying...")
    except:
        print("Something went wrong.")
    finally:
        print("Done!")
print("Loop ended.")
# Prints trying...
# Prints Done!
# Prints trying...
# Prints Done!
# Prints Loop ended.
