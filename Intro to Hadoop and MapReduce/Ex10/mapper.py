#!/usr/bin/python
import sys
from datetime import datetime


def mapper():
	salesWeekDay = dict()

	# file =  open("/Users/cinq/Desktop/SharedVM/testFile", "r")
	# file =  open("/Users/cinq/Desktop/SharedVM/testForum", "r")

	print "mapper"


	# for line in file:

	for line in sys.stdin:
		data = line.strip().split("\t")

		date, time, store, item, cost, payment = data

		weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

		print "{0}\t{1}".format(weekday, float(cost))


mapper()
