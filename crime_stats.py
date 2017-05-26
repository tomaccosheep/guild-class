#Advanced: Create a Jupyter Notebook with a graph of the crime breakdown using matplotlib.

import os
import csv
import operator

# Make a list of dictionaries, with each dictionary containing information about an instance of crime {{
crimelist = [] 
for i in os.listdir('pdx_crime_data/data'):
	with open('pdx_crime_data/data/' + i, mode='r') as infile:
		readcrime = csv.DictReader(infile)
		for rows in readcrime:
			crimelist.append(rows)	
# }}

# Make a list of seen crimes and years, and make two dictionaries:
# Make a dictionary where the keys are crimes, and make a dictionary
# Where the keys are years. For each dictionary, the values are counters
# iterated with each instance found {{
rate_type = {}
rate_year = {}
not_orig_type = []
not_orig_year = []
# }}

# Check crimelist, check keys against not_orig lists, add to list if orig
# update rate dictionaries by adding 1 if not orig {{
for i in crimelist:
	if i['Major Offense Type'] not in not_orig_type:
		new_type = i['Major Offense Type']
		rate_type[new_type] = 1
		not_orig_type.append(new_type)
	if i['Major Offense Type'] in not_orig_type:
		old_type = i['Major Offense Type']
		rate_type[old_type] += 1	
	if i['Report Date'][-4:] not in not_orig_year:
		new_year= i['Report Date'][-4:]
		rate_year[new_year] = 1
		not_orig_year.append(new_year)
	if i['Report Date'][-4:] in not_orig_year:
		old_year = i['Report Date'][-4:]
		rate_year[old_year] += 1
# }}		


# Put the dictionaries into tuples, order them, and then print them {{
sorted_type = sorted(rate_type.items(), key=operator.itemgetter(1))
print('Most common crime: ' + sorted_type[-1][0])
print('Least common crime: ' + sorted_type[0][0])
sorted_year = sorted(rate_year.items(), key=operator.itemgetter(1))
print('Worst year for crime: ' + sorted_year[-1][0])
# }}
