import csv

with open("myDict.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
