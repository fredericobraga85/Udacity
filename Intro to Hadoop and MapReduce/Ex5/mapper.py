#!/usr/bin/python
import sys
import re

def mapper():

	totalHitsDict = dict()

	# file =  open("/Users/cinq/Desktop/SharedVM/access_log", "r")

	totalHits = 0

	# for line in file:
	for line in sys.stdin:

		# data = line.strip().split("\t")

		regex = '([(\d\.)]+) (.*?) (.*?) \[(.*?)\] "(.*?)" ([0-9]+|-) ([0-9]+|-)'

		match = re.match(regex, line)

		if match != None:
			lineGroup = match.groups()

			if 'assets/js/the-associates.js' in lineGroup[4]:
				totalHits += 1

	totalHitsDict["totalHits"] = totalHits

	for key, value in totalHitsDict.iteritems():
		print "{0}\t{1}".format(key, value)

	# 	if len(data) == 6:
	# 		date, time, store, item, cost, payment = data
    #
	# 		totalSales += 1
	# 		totalValueSales += float(cost)
    #
    #
	# salesDict["totalSales"] = totalSales
	# salesDict["totalValueSales"] = totalValueSales



mapper()
