import csv

with open("myRead.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
