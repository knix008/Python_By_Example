# in a for Statement
for x in range(2):
    try:
        print("trying...")
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
