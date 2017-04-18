#!/usr/bin/python
import sys
import re

def mapper():

	totalHitsDict = dict()

	file =  open("/Users/cinq/Desktop/SharedVM/forum_node.tsv", "r")
	# file =  open("/Users/cinq/Desktop/SharedVM/testForum", "r")

	completeLine = ""
	count = 1

	fantasticCount = 0
	nodes = []


	for line in file:
	# for line in sys.stdin:
		if count == 1:
			count += 1
			continue

		completeLine += line

		if line[-5:-2] == "\"t\"" or line[-5:-2] == "\"f\"":

			data = completeLine.strip().split("\t")

			id = data[0]
			body = data[4].replace("\n","")
			listBody = replaceBody(body, ['.', ',', '!', '?' , ':', ';', '\"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-', '/'])

			count = listBody.count('fantastic')

			if count > 0:
				fantasticCount += listBody.count('fantastic')
				# print id, count, fantasticCount, listBody

			if listBody.count('fantastically') > 0:
				nodes.append(int(id.replace('"', '')))

			completeLine = ""

		else:
			continue


		# data = line.strip().split("\"\t\"")

		# id, title, tagname, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, active_revision_id, extra, extra_ref_id, extra_count, marked = data
		# print line
		# id = data[0]
		# body = data[5]

		# print id, body

	print fantasticCount
	print nodes

	for key, value in totalHitsDict.iteritems():
		print "{0}\t{1}".format(key, value)


def replaceBody(body, list):

	result = body

	for simbol in list:
		result = result.replace(simbol, ' ')

	return result.lower().split()


mapper()
