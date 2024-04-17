import csv

with open("myWrite.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Bob", "25", "Manager", "Seattle"])
    writer.writerow(["Sam", "30", "Developer", "New York"])
    writer.writerow(["Kwon", "53", "Engineer", "Seoul"])
