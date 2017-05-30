#An account will be a class named Account in a module named account: it will have private attributes for the balance and interest rate. Remember to underscore _ prefix any private attributes. A newly-instantiated account will have zero balance and an interest rate of 0.1%.
#Write class methods in the account class that:
#
#I've already written out some test code that will check that your Account class behaves as expected. Save it as account_test.py in your solution directory. These tests should all pass for your Account implementation. Either run py.test from the atm-interface directory, or setup a PyCharm test Run Configuration.
#
#You should still write doctests for your functions that test internal implementation. E.g. Check that internal variables are set correctly. My classes can't do that since internal variables are not part of the defined behavior.
#

class Account(object):
	def __init__(self, balance):
		self._balance = balance
		self._interest_rate = .01
	def __str__(self):
		return 'Your balance is {}'.format(self._balance)
	def getfunds(self):
		return print(self._balance)
	def deposit(self, more_money):
		self._balance += more_money
		return print(self._balance)
	def check_withdrawal(self, amount):
		if self._balance >= amount:
			return print(True), True
		else:
			return print(False), False
	def withdraw(self, amount):
		if self._balance >= amount:
			self._balance -= amount
			return print('Your balance is {}.'.format(self._balance))
		else:
			print('You don\'t have that much money')
			return ValueError
	def calc_interest(self, days):
		_out = self._balance * ( (1 + 1 / ( days * 100 ) ) ** days )
		return print(_out)



#Advanced
#
#Write a program that functions as a simple ATM for two accounts:
#
#Checking account
#Savings account
#Implement a user interface in a module main that lets a user pick each of those actions for a given account and updates the account. After each action it will print the balance.
#
#Super Advanced
#
#Adds some advanced features to the account class.
#
#Add a function called get_standing() have it return a bool with whether the account has less than $1000 in it.
#
#Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.
#
#Save the account balance to a file after each operation. Read that balance on startup so the balance persists across program starts.
#
#Add to each account class an account ID number.
#
#Allow the user to open more than one account. Let them perform all of the above operations by account number.
#
#With each advanced feature, of course add doctests, but also expand the TestAccountBehavior with new behavior test functions.
