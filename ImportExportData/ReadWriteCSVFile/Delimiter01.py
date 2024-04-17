# Write a file with different delimiter '|'
import csv

with open("myDelimiter01.csv", mode="w") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["Bob", "25", "Manager", "Seattle"])
    writer.writerow(["Sam", "30", "Developer", "New York"])
    writer.writerow(["Kwon", "53", "Engineer", "Seoul"])
