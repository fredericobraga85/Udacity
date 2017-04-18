#!/usr/bin/python
import sys

totalHits = 0

totalHitsDict = dict()

for line in sys.stdin:

    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    key , value = data

    if key in totalHitsDict:
        totalHitsDict[key] += int(value)
    else:
        totalHitsDict[key] = int(value)

for key, value in totalHitsDict.iteritems():
    print "{0}\t{1}".format(key, value)