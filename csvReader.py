import csv

csvFile = 'Activities.csv'

for row in csv.reader(open(csvFile)):
    print(row)
