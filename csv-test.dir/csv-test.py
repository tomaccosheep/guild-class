import csv
with open('google.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Name'], row['Phone 1 - Value'], row['E-mail 1 - Value'])
