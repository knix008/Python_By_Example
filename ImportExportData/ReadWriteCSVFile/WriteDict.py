import csv

with open("myDictWrite.csv", mode="w") as f:
    keys = ["name", "age", "job", "city"]
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()  # add column names in the CSV file
    writer.writerow({"job": "Manager", "city": "Seattle", "age": "25", "name": "Bob"})
    writer.writerow(
        {"job": "Developer", "city": "New York", "age": "30", "name": "Sam"}
    )
    writer.writerow({"job": "Engineer", "city": "Seoul", "age": "53", "name": "Kwon"})
