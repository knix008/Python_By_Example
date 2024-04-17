import csv

with open("myQuote01.csv") as f:
    reader = csv.reader(f, quotechar='"')
    for row in reader:
        print(row)
