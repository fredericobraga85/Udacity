#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint
import os.path
enron_data = pickle.load(open(os.path.dirname(__file__) + "/../final_project/final_project_dataset.pkl", "r"))
poi_names = open(os.path.dirname(__file__) + "/../final_project/poi_names.txt", "r")

totalPoi = []


enron_data_count = 0;
for k, v in enron_data.iteritems():
    if isinstance(v, dict):
        pprint.pprint(v)
        break
        
#pprint.pprint(enron_data["PRENTICE JAMES"]["total_stock_value"])    Wesley Colwell
pprint.pprint(enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"])

        
#        for k1, v1 in v.iteritems():
#            if(k1 == "poi" and v1 == 1):
#                pprint.pprint(str(v1) + " " + k)
#                enron_data_count += 1

#print "enron_data_count =", enron_data_count

#poi_name_count = 0
#with poi_names as f:
#   for line in f:
#        print line.replace("\n", ""), '(y)' in line, 'n' in line
#        if '(y)' in line or '(n)' in line:
#            print "line", line.replace("\n", "") , poi_name_count
#            poi_name_count += 1
#
#print "poi_name_count =", poi_name_count


#totalPoi = (enron_data_count - poiAlreadyCount
#print "totalPoi =", 
#print totalPoi

#pprint.pprint(enron_data.values()[0])


