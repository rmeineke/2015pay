#! /usr/bin/python3
import csv

filename = '2015.pay.csv'
with open(filename, 'r', encoding='utf-8') as fin:
    reader = csv.reader(fin)
    row1 = next(reader)
    print(row1)