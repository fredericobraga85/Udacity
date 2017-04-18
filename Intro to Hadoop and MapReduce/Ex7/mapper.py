#!/usr/bin/python
import sys
import re

def mapper():

	totalHitsDict = dict()

	# file =  open("/Users/cinq/Desktop/SharedVM/testFileLog", "r")

	# for line in file:
	for line in sys.stdin:

		# data = line.strip().split("\t")

		regex = '([(\d\.)]+) (.*?) (.*?) \[(.*?)\] "(.*?)" ([0-9]+|-) ([0-9]+|-)'

		match = re.match(regex, line)

		if match != None:
			lineGroup = match.groups()

			path = lineGroup[4].split(" ")[1].replace("http://www.the-associates.co.uk", "")

			if path in totalHitsDict:
				totalHitsDict[path] += 1
			else:
				totalHitsDict[path] = 1

	for key, value in totalHitsDict.iteritems():
		print "{0}\t{1}".format(key, value)


mapper()
