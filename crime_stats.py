#Lab: Portland Crime Data Analysis
#
#Delivery Method: Prompt and Dataset
#
#Goal
#
#Analyize the city of Portland, OR public dataset of recorded crimes for most common crime, rarest crime(s), and the year with most crime.
#
#Instructions
#
#The City of Portland has keeps track of crimes in a publicly available dataset!
#
#Print out a summary of the data:
#
#The specific most common crime type.
#The rarest crimes.
#The year with the most crime.
#Advanced
#
#Create a Jupyter Notebook with a graph of the crime breakdown using matplotlib.
#Documentation
#
#Python Official Docs: Operators
#Key Concepts
#
#Concept One
#A Good Idea
#A Tough One
import os
crimebook = {}
a = os.listdir('pdx_crime_data/data')
for i in a:
	with open(i, mode='r') as infile:
	readcrime = csv.DictReader(infile)
	for rows in readcrime:
		crimebook



