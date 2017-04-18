# !/usr/bin/python
import sys

highestCost = 0

storeCostDict = dict()

for line in sys.stdin:

    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    store, cost = data

    if store in storeCostDict:
        if storeCostDict[store] < cost:
            storeCostDict[store] = cost
    else:
        storeCostDict[store] = cost

for key, value in storeCostDict.iteritems():
    print "{0}\t{1}".format(key, value)


