#!/usr/bin/python3
import csv

payfile = open('2015.pay.csv')
payreader = csv.reader(payfile)

count = 0
for row in payreader:
    if 'Fire' in str(row[1]) and ('PSRD' in str(row[2]) or 'PSCS' in str(row[2]) or 'PSD' in str(row[2]) or 'Comm.' in str(row[2])):
        count += 1
        print('{:3} -- {:30} -- {:6} -- {:9} -- {:>10} -- {:>10} -- {:>9}' \
              .format(count, str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
