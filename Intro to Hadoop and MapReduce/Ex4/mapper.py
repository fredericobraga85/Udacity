#!/usr/bin/python
import sys

def mapper():

	salesDict = dict()

	file =  open("/Users/cinq/Desktop/SharedVM/purchases.txt", "r")

	totalSales = 0
	totalValueSales = 0

	for line in file:

	# for line in sys.stdin:

		data = line.strip().split("\t")
		
		if len(data) == 6:
			date, time, store, item, cost, payment = data

			totalSales += 1
			totalValueSales += float(cost)


	salesDict["totalSales"] = totalSales
	salesDict["totalValueSales"] = totalValueSales

	for key, value in salesDict.iteritems():
			print "{0}\t{1}".format(key,value)


mapper()
