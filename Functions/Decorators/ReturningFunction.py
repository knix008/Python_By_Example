def greet():
    def hello(name):
        print("Innter : Hello", name)

    return hello


greet_user = greet()

greet_user("Bob")
# Prints Hello Bob
