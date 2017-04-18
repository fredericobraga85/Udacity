#!/usr/bin/python
import sys

def mapper():

	storeCostDict = dict()

	file =  open("/Users/cinq/Desktop/SharedVM/purchases.txt", "r")
	for line in file:

	# for line in sys.stdin:

		data = line.strip().split("\t")
		
		if len(data) == 6:
			date, time, store, item, cost, payment = data

			if selectedStore(store):

				c = float(cost)

				if store in storeCostDict:
					if storeCostDict[store] < c:
						storeCostDict[store] = c
				else:
					storeCostDict[store] = c

	for key, value in storeCostDict.iteritems():
			print "{0}\t{1}".format(key,value)


def selectedStore(store):

	selectedStores = ["Reno", "Toledo", "Chandler"]

	if store in selectedStores:
		return True
	else:
		return False


mapper()
