#6) Search isn't working
#9) Crashes when not everyone has values
import csv


# Create empty phonebook {
phonebook = {}
# }


# Import the csv file {
try:
	with open('google.csv', mode='r') as infile:
			reader = csv.DictReader(infile)
			for rows in reader:
					phonebook[rows['Name']] = { 'number' : rows['Phone 1 - Value'],\
							'phrase' : rows['E-mail 1 - Value'] }
# }


	# Print phonebook for verification {
	print(phonebook)
	# }


# Catch key errors if csv import fails {
except KeyError:
		print('key error, didn\'t import csv')
# }


# Set status for while loop {
running = True
while running:
# }


	# Input prompt {
	query = input('Enter:\n\
1) to add someone to the phonebook\n\
2) to look up someone\'s information\n\
3) to modify someone\'s information\n\
4) to delete a person\n\
5) to look up a specific piece of information\n\
6) to search for a phone number or email\n\
7) to view the full phonebook\n\
8) to quit\n\
9) to save phonebook to csv\n\
: ')
	# }


	# 1) Add someone to the phonebook {
	if query == '1':
		new_name = input('Enter the person\'s name: ')
		phonebook[new_name] = {}
		new_num = input('Enter the person\'s number: ')
		phonebook[new_name]['number'] = new_num
		new_phrase = input('Enter the person\'s phrase: ')
		phonebook[new_name]['phrase'] = new_phrase
		print(phonebook)
	# }


	# 2) Look up someone's information {
	elif query == '2':
		get_name = input('Which user would you like to look up? ') 
		# Try to look up the name, catch key errors {
		try:
			print(phonebook[get_name])
		except KeyError:
			print('There is no one by that name in this phonebook. ')
			continue
		# }
	# }


	# 3) Modify someone's information {
	elif query == '3':
		print(phonebook)


		# Get information to change {
		change_name = input('Who\'s info would you like to change? ')
		name_info_del = input('Type 1 to change their name, 2 to change their info, or 3 to delete info :')
		# }


		# 1) Change someone's name by copying information and deleting name {
		if name_info_del == '1':
			change_name_new = input('What is the corrected name? ')
			print(change_name + ' ' + change_name_new)
			try:
				phonebook[change_name_new] = phonebook[change_name]
				del phonebook[change_name]
			except KeyError:
				continue
		# }


		# 2) Change one piece of information about someone {
		elif name_info_del == '2':
			change_info = input('What would you like to change? ')
			try:
				del phonebook[change_name][change_info]
				phonebook[change_name][change_info] = input('What should that value be? ')
			except KeyError:
				print('Failed2')
				continue
		# }


		# 3) Delete someone from the phonebook {
		elif name_info_del == '3':
			print(phonebook[change_name])
			del_info = input('You would like to delete their ')
			try:
				del phonebook[change_name][del_info]
			except KeyError:
				print('Failed')
				continue
		# }


		# Catch input that isn't 1, 2, or 3 {
		else:
			print('That wasn\'t 1, 2, or 3!')
		# }
	# }


	# 4) Delete a person {
	elif query == '4':
		try:
			del_name = input('Which user would you like to delete? ')
			del phonebook[del_name]
		except KeyError:
			continue
	# }


	# 5) Look up specific information about a person {
	elif query == '5':
		lookup_name = input('Who would you like to look up? ')
		lookup_key = input('What would you like to look up about them? ')
		try:
			print(phonebook[lookup_name][lookup_key])
		except KeyError:
			continue
	# }


	# 6) Search non-key values of the dictionary {
	elif query == '6':
		search_category = input('What category would you like to search? ')
		search_string = input('What string would you like to search for? ')
		try:
			for i in phonebook.items():
				#print(i[1])
				if str(i[1][search_category]).find(search_string):
					print(search_category, search_string, str(i[1][search_category]).find(search_string))
					print(i[0], '\n', i[1][search_category])
		except KeyError:
			continue
	# }


	# 7) Print the entire phonebook {
	elif query == '7':
		print(phonebook)
	# }


	# 8) Quit {
	elif query == '8':
		quit()
	# }


	# 9) Save info to csv {
	elif query == '9':


		# Open the csv file so that it's writable, and introduce fieldnames {
		with open('out.csv', 'w') as csvfile:
			fieldnames = ['Name', 'Phone 1 - Value', 'E-mail 1 - Value']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
		# }


		# Use a for loop to export dictionary info to rows {
			for i in phonebook:
				#writer.writerow()
				print(i, '\n', phonebook[i]['number'])
				writer.writerow({'Name': i, 'Phone 1 - Value': phonebook[i]['number'], 'E-mail 1 - Value': phonebook[i]['phrase']})
		# }
	# }

	
	# Catch if the original prompt's input isn't 1 through 9 {
	else:
		print('I did not understand that.')
	# }
