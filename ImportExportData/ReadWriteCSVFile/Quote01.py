import csv

with open("myQuote01.csv", mode="w") as f:
    writer = csv.writer(f, quotechar='"')
    writer.writerow(["Bob", "25", "113 Cherry St, Seattle, WA 98104, USA"])
    writer.writerow(["Sam", "30", "150 Greene St, New York, NY 10012, USA"])
    writer.writerow(["Kwon", "53", "411 Bongeunsaro, Seoul, Kangnamgu, South Korea"])
