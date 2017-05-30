

# Make an account object for a user {{

class Account(object):
	def __init__(self, balance):
		self._balance = balance
		self._interest_rate = .001
		self._bank_fees = 0
		self._ID = 0


	def __str__(self):
		return 'Your balance is {}'.format(self._balance)


	# Make a get_standing function to see if fees should apply {{
	def get_standing(self):
		if self._balance < 1000:
			return True
		elif self._balance >= 1000:
			return False
		else:
			return ValueError
	# }}


	def getfunds(self):
		return print(self._balance)


	# {{ deposit money, add fees if get_standing returns true
	def deposit(self, more_money):
		if self.get_standing():
			if self._balance + more_money > 5:
				self._balance += more_money
				self._balance -= 5
				self._bank_fees += 5
				return print(self._balance)
			else:
				return print('You don\'t have enough to pay the fees.')
		else:			
			self._balance += more_money
			return print(self._balance)
	# }}

	# Check if money can be withdrawn, keeping in mind that
	# There will be a fee if you have under 1000 (done through
	# get_standing() {{
	def check_withdrawal(self, amount):
		if self.get_standing():
			if self._balance > 5 + amount:
				return print(True), True
			else:
				return print(False), False
		elif self._balance >= amount:
			return print(True), True
		else:
			return print(False), False
	# }}

	# Withdraw money, and pay $5 fee if under $1000 {{
	def withdraw(self, amount):
		if self.get_standing():
			if self._balance > 5 + amount:
				self._balance -= 5 + amount
				self._bank_fees += 5
				return print('Your balance is {}.'.format(self._balance))
			else:
				return print('You don\'t have enough money.')
		elif self._balance >= amount:
			self._balance -= amount
			return print('Your balance is {}.'.format(self._balance))
		else:
			print('You don\'t have that much money')
			return ValueError
	# }}


	def calc_interest(self, days):
		_out = self._balance * ( (1 + 1 / ( days * 1000 ) ) ** days )
		return print(_out)


	# Transfer from another account to this one, if
	# They have enough money. It calls on transto to do every
	# transfer.
	# {{
	def transfrom(self, other_acc, trans_num):
		if self.get_standing() and self._balance + trans_num > 5:
			try:
				other_acc.transto(self, trans_num)
				return
			except:
				print('Transfer failed.')
				return
		elif self.get_standing():
			return print('You don\'t have enough money to do that')
		else:
			other_acc.transto(self, trans_num)
			return
	# }}


	# Transfer from this account to another, if
	# this account has enough money {{
	def transto(self, other_acc, trans_num):
		if self.get_standing() and self._balance < trans_num + 5:
			return print('You don\'t have enough money.')	
		elif self._balance < trans_num:
			return print('You don\'t have enough money.')	
		elif self.get_standing():
			self._balance -= 5
			self._bank_fees += 5
			self._balance -= trans_num
			other_acc.deposit(trans_num)
			return
		else:
			self._balance -= trans_num
			other_acc.deposit(trans_num)
			return
	# }}
	

	# Return bank fees (used when checking out) {{
	def return_fees(self):
		return self._bank_fees
	# }}


	# Set an ID number for the account {{
	def import_ID(self, number):
		self._ID = number
		return
	# }}

	# Return the ID number {{
	def export_ID(self):
		return self._ID
	# }}

