#!/usr/bin/python
import sys
import time

totalSalesWeekDay = dict()

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    key , value = data

    totalSalesWeekDay[key] = totalSalesWeekDay.get(key, 0 ) + float(value)


for key, value in totalSalesWeekDay.iteritems():

    print  "{0}\t{1}".format(key, totalSalesWeekDay[key])


