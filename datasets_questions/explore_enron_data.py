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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

len(enron_data) # count number of person

len(enron_data.values()[0])  # count features per key(person)

count = 0               #count the number of POI 
for i in enron_data.values():
    if i['poi'] == True:
        count += 1

enron_data['PRENTICE JAMES']['total_stock_value']  #stock belong to ...
enron_data['COLWELL WESLEY']['from_this_person_to_poi']  #
enron_data['SKILLING JEFFREY K']['exercised_stock_options']

enron_data['SKILLING JEFFREY K']['total_payments']
enron_data['FASTOW ANDREW S']['total_payments']
enron_data['LAY KENNETH L']['total_payments']

count = 0               #count the number of people do not have salary data
for i in enron_data.values():
    if i['salary'] != 'NaN':
        count += 1

count = 0               #count the number of people do not have email
for i in enron_data.values():
    if i['email_address'] != 'NaN':
        count += 1

count = 0               #count the number of people do not have email
for i in enron_data.values():
    if i['total_payments'] == 'NaN':
        count += 1
float(count)/len(enron_data)


sorted(enron_data.keys())