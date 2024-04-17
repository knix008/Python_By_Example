import csv

with open("myWrite.csv") as f:
    keys = ["name", "age", "job", "city"]
    reader = csv.DictReader(f, fieldnames=keys)
    for row in reader:
        print(row)
