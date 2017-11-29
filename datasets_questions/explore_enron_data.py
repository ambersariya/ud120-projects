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
import numbers
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


print("# of people", len(enron_data))
print('# of features/person: ', len(enron_data[list(enron_data.keys())[0]]))

# pois = { key:value for key, value in enron_data if value['poi'] == True }
# print('# of Persons of interest (POI): ', len(pois))
num_pois = 0
for p in enron_data:
    person = enron_data[p]

    if (person['poi'] == True):
        num_pois += 1

print('# of Persons of interest (POI): ', num_pois)


#Quiz 16

poi_names = open("../final_project/poi_names.txt").read().split('\n')
poi_y = [name for name in poi_names if "(y)" in name or "(n)" in name]
print("Total number of POIs:", len(poi_y))

# Quiz 18 - Query the dataset 1
# Question - What is the total value of the stock belonging to James Prentice?
print('What is the total value of the stock belonging to James Prentice? ',enron_data['PRENTICE JAMES']['total_stock_value'])

# Quiz 19 - How many email messages do we have from  to persons of interest?
print('How many email messages do we have from  to persons of interest? ', enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# Quiz 20
print(' What’s the value of stock options exercised by Jeffrey K Skilling? ', enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# Quiz 25:  How much money did that person (Lay, Skilling and Fastow) get?
# how_much_money = [name for name in enron_data if "LAY" in name or "SKILLING" in name or "FASTOW" in name]
how_much_money = {k:v for k,v in enron_data.items() if "LAY" in k or "SKILLING" in k or "FASTOW" in k}

print(how_much_money)

#Quiz 27
# isinstance(x, Number)
people_with_quanitified_salaries = {k:v for k,v in enron_data.items() if isinstance(v['salary'], numbers.Number)}
print('How many folks in this dataset have a quantified salary?', len(people_with_quanitified_salaries))

people_with_emails = {k:v for k,v in enron_data.items() if '@' in v['email_address']}
print('How many folks in this dataset have a email?', len(people_with_emails))

#Quiz 29
people_with_nan_payments = {k:v for k,v in enron_data.items() if v['total_payments'] == 'NaN'}
pct_people_with_nan_payments = len(people_with_nan_payments)/len(enron_data) * 100
print('what percentage of people in the E+F dataset (as it currently exists) have “NaN” for their total payments?', "{0} people which is {1:.1f}%".format(len(people_with_nan_payments), pct_people_with_nan_payments))


#Quiz 30
#How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
pois_with_nan_payments = {k:v for k,v in enron_data.items() if v['total_payments'] == 'NaN' and v['poi'] == True}
pct_pois_with_nan_payments = (len(pois_with_nan_payments) / num_pois) * 100

print('How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?', "{0} POIs with NaN payments which is {1:.01}%".format(len(pois_with_nan_payments), pct_pois_with_nan_payments))

