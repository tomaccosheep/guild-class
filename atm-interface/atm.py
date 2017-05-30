import account

running = 1
while running = 1:
	checking_value = int(input('How much money is in your checking account?\n:'))
	savings_value = int(input('How much money is in your savings account?\n:'))
	if checking_value >= 0 and savings_value >= 0:
		running = 0
	else:
		print('All numbers must be greater than or equal to zero.')

checking = account.Account(checking_value)
savings = account.Accounnt(savings_value)

running = 1
while running = 1:
	print('Choose an option:\n\
1.
'


#Implement a user interface in a module main that lets a user pick each of those actions for a given account and updates the account. After each action it will print the balance.

#Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.
#
#Save the account balance to a file after each operation. Read that balance on startup so the balance persists across program starts.
#
#Add to each account class an account ID number.
#
#Allow the user to open more than one account. Let them perform all of the above operations by account number.

