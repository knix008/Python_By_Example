# Read a file with different delimiter '|'
import csv

with open("myDelimiter01.csv") as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        print(row)
