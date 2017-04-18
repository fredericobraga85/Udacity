#!/usr/bin/python
import sys

highestCost = 0

salesDict = dict()

for line in sys.stdin:

    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    key , value = data

    if key in salesDict:
        salesDict[key] += value
    else:
        salesDict[key] = value

for key, value in salesDict.iteritems():
    print "{0}\t{1}".format(key, value)