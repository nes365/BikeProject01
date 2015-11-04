# imports
import csv
# constants
csvfile = 'Activities.csv'


def readcsv(csvfile):
    """

    :param csvfile:
    """
for row in csv.reader(open(csvfile)):
    print(row)


def cmds = dict():
for row in csv.reader(open(csvfile)):
    try:
        cmds[row[0]] += 1
    except KeyError:
        cmds[row[0]] = 1
return cmds
