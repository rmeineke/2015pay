#!/usr/bin/python3
import csv
import sys

payfile = open('2015.pay.csv')
payreader = csv.reader(payfile)

while True:
    payfile.seek(0)
    searchfor = input('{}'.format('Enter name: '))
    if searchfor == 'q':
        sys.exit(0)

    searchfor = searchfor.lower()
    count = 0
    for row in payreader:
        # print(type(row))
        name = str(row[0])
        name = name.lower()
        if searchfor in name:
            count += 1
            print('{:3} -- {:30} -- {:6} -- {:9} -- {:>10} -- {:>10} -- {:>9}' \
                  .format(count, str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
    print()
