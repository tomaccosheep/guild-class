#to do:
# - Partial Name
# - Phone Number
# - Partial Phrase
#- Add Save and Load features for your contact data by saving a csv file.

#import csv
#running = True
#phonebook = {}
#while running:
## ;)
#
#	try:
#		query = int(input('Enter: \n1) to add a new person to the \
#phonebook\n2) to look up someone\'s information\n3) to modify someone\'s \
#information\n4) to delete a person\n5) to look up a \
#specific piece of information\n6) import a csv file\n7) to view full phonebook\n8) quit\n\
#9) look at tuples: '))
#
#	except ValueError:
#		print('Input must be a number. Please try again.')
#		continue
#
#
#	if query == 1:
#		new_name = input('Enter the person\'s name: ')
#		phonebook[new_name] = {}
#		
#		new_num = input('Enter the person\'s number: ')
#		phonebook[new_name]['number'] = new_num
#		new_phrase = input('Enter the person\'s phrase: ')
#		phonebook[new_name]['phrase'] = new_phrase
#		print(phonebook)
	elif query == 2:
		get_name = input('Which user would you like to look up? ')
		try:
			print(phonebook[get_name])
		except KeyError:
			print('There is no one by that name in this phonebook. ')
			continue
	elif query == 3:
		print(phonebook)
		change_name = input('Who\'s info would you like to change? ')
		name_info_del = input('Type 1 to change their name, 2 to change their info, or 3 to delete info :')
		if name_info_del == '1': 
			change_name_new = input('What is the corrected name? ')
			print(change_name + ' ' + change_name_new)
			try:
				phonebook[change_name_new] = phonebook[change_name]
				del phonebook[change_name]
			except KeyError:
				continue
			#change the name by getting a new name, copying information,
			#and deleting name
		elif name_info_del == '2': 
			change_info = input('What would you like to change? ')
			try:
				del phonebook[change_name][change_info]
				phonebook[change_name][change_info] = input('What \
should that value be? ')
			except KeyError:
				print('Failed2')
				continue
			#change a piece of their info in the dictionary
		elif name_info_del == '3': 
			print(phonebook[change_name])
			del_info = input('You would like to delete their ')
			try:
				del phonebook[change_name][del_info]
			except KeyError:
				print('Failed')
				continue
			#delete a piece of information
		else:
			print('That wasn\'t 1, 2, or 3!')
#	elif query == 4:
#		try:
#			del_name = input('Which user would you like to delete? ')
#			del phonebook[del_name]
#		except KeyError:
#			continue
#	elif query == 5:
#		lookup_name = input('Who would you like to look up info about? ')
#		lookup_key = input('What would you like to look up about them? ')
#		try:
#			print(phonebook[lookup_name][lookup_key])
#		except KeyError:
#			continue
	#elif query == 6:
	#	input_file = input('What is the name of the file you\'d like to input? ')
	#	try:
	#		with open(input_file, mode='r') as infile:
	#			reader = csv.DictReader(infile)
	#			for rows in reader:
	#				phonebook[rows['Name']] = { 'number' : rows['Phone 1 - Value'], 'phrase' : rows['E-mail 1 - Value'] }	
#with open('coors.csv', mode='r') as infile:
#    reader = csv.reader(infile)
#    with open('coors_new.csv', mode='w') as outfile:
#        writer = csv.writer(outfile)
#        mydict = {rows[0]:rows[1] for rows in reader}
#		except KeyError:
#			continue
#	elif query == 7:
#		print(phonebook)
#	elif query == 8:
#		quit()
	elif query == 9:
		searchkey = input('Which part would you like to search? ')
		searchstring = input('What string would you like to search for? ')
		for i in phonebook.items():
			print(i)
			phonei = i[1][searchkey] 
			if str(i[1][searchkey]).find(searchstring):
				print(i + '\n' + i[1][searchkey])
	else:
		print('I did not understand that.')
