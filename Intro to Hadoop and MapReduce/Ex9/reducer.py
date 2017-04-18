#!/usr/bin/python
import sys
import numpy
import time

totalSalesWeekDay = dict()

print "reducer"
start_time = time.time()
for line in sys.stdin:



    data = line.strip().split("\t")

    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    key , value = data

    if key in totalSalesWeekDay:
        totalSalesWeekDay[key].append(float(value))
    else:
        totalSalesWeekDay[key] = [float(value)]

for key, value in totalSalesWeekDay.iteritems():

    a = numpy.array(value)
    # print a
    print numpy.mean(a)

elapsed_time = time.time() - start_time
print "reducer end" , elapsed_time
# print "{0}\t{1}".format(mostPopularPath, numberOccurrences)