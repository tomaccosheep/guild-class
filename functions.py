def greeting_to_person(name, phone):
	print('Hello {}'.format(name))
	print('I will call you at ' + phone[0:5] + '... Actually that\'s too much work.')

your_name = input('What is your name? ')
your_phone_number = input('What is your phone number? ')

final = greeting_to_person(your_name, your_phone_number)
print(final)
