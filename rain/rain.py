#Print out a summary of the data:
#
#The specific date with the most rain.
#The year with the most rain.
#Note:
#
#The header has a totally different format than the data itself. You will have to slice out the header lines from all the lines you read.
#
#You can split a string by whitespace into a list of strings using .split().
#
#Extract the date sting from the date columns.
#
#If there are any days with - for data, explicitly drop them from your dataset.
#
#Avoid using un-named "pairs" outside of dictionaries.
#
#If you need to group together individual instances of a date and a rainfall amount use a tuple! ( Or perhaps look at the namedtuple form collections. )
#
#Advanced
#
#Find and print the day of the year with the most rain on average. E.g. December 30th has 1" of rain on average.
#
#Allow someone to type in a date in the future and, using the average value for that day of the year, predict the amount of rain.
#
#Super Advanced
#
#URL open the main listing website. Parse it and allow the user to select statistics from the available rain gauges.
#Python gives you a module called urllib.request you can use a function urllib.request.urlopen(url) which returns a file-like object. Look at the docs for that module.
#
#One little difference is the file-like object doesn't return strings, it returns bytes. The following code snippet reads Pride and Prejudice into a list of strings:
#
#import urllib.request
#
#with urllib.request.urlopen('http://www.gutenberg.org/ebooks/1342.txt.utf-8') as pride_and_prejudice_file:
#  lines = [byte_line.decode('utf-8') for byte_line in pride_and_prejudice_file]
#Read up on using Pip and PyPI and installing third-party packages. Use the beautifulsoup package to parse the HTML of that page. You shouldn't hard code in any input other than the listing URL.





import os
from bs4 import BeautifulSoup
import http.client
import subprocess
cli_out = subprocess.check_output(['bash \'fortune && fortune\''])
#cli_out = subprocess.check_output(['elinks -source https://or.water.usgs.gov/non-usgs/bes/|grep \'rain"\'|cut -d\'"\' -f2'])
print(cli_out)
#	print(str(i) + 'aaa')
#	if i != 0:
#		web_data = http.client.HTTPConnection('https://or.water.usgs.gov/non-usgs/bes/' + str(i))
#		print('a')
#		soup = BeautifulSoup(web_data, 'html.parser')
#		print('b')
