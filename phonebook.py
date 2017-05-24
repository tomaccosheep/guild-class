running = True
phonebook = {}
while running:
# ;)

	try:
		query = int(input('Enter: \n1) to add a new person to the \
phonebook\n2) to look up someone\'s information\n3) to modify someone\'s \
information\n4) to delete a person\n5) to look up a \
specific piece of information\n6) to quit\n: '))

	except ValueError:
		print('Input must be a number. Please try again.')
		continue


	if query == 1:
		new_name = input('Enter the person\'s name: ')
		phonebook[new_name] = {}
		
		new_num = input('Enter the person\'s number: ')
		phonebook[new_name]['number'] = new_num
		new_phrase = input('Enter the person\'s phrase: ')
		phonebook[new_name]['phrase'] = new_phrase
		print(phonebook)
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
			phonebook[change_name_new] = phonebook[change_name]
			del phonebook[change_name]
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
	elif query == 4:
		del_name = input('Which user would you like to delete? ')
		del phonebook[del_name]
	elif query == 5:
		lookup_name = input('Who would you like to look up info about? ')
		lookup_key = input('What would you like to look up about them? ')
		print(phonebook[lookup_name][lookup_key])
	elif query == 6:
		quit()
	else:
		print('I did not understand that.')
