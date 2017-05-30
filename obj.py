# This declares an object called 'Person' that returns their name as a string or list {{
class Person(object):
	def __init__(self, name):
		self.name = name
	def print_name(self):
		print(self.name)
	def __str__(self):
		return 'My name is {}'.format(self.name)
	def __repr__(self):
		return 'My name *really* is {}'.format(self.name)
# }}

# This part tests out the usage of the person object. Also, objects are made within the class that weren't defined by the class {{
chris = Person('Chris')
chris.phone = '503.277-9710'
chris.print_name()
print(chris.phone)
chris.name = 'NotChris'
chris.print_name()
# Experiment with strings and lists being returned {{
print(chris)
print([chris])
# }}
# }}


# This is a class called 'BankAccount' {{
class BankAccount:
	# This is a method that initializes the object {{
	def __init__(self, balance, acc_name):
		self.balance = balance
		self.acc_name = acc_name
	# }}
	# This returns the string version {{
	def __str__(self):
		return 'Hello {}, your balance is ${}'.format(self.acc_name, self.balance)
	# }}
	# This defines the 'withdraw' method {{
	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			print('Thank you {}. Your remaining balance is {}.'.format(self.acc_name, self.balance))
		else:
			print('Sorry, you don\'t have that much money.')
	# }}
	def deposit(self, amount):
		self.balance += amount
		print('Thank you {}. Your remaining balance is {}.'.format(self.acc_name, self.balance))
# }}


# This is a subclass of BankAccount {{
class BankAccountSpecial(BankAccount):
	# This initializes BankAccountSpecial {{
	def __init__(self, balance, acc_name):
		super().__init__(balance, acc_name)
	# }}
	# This redefines withdraw from the class {{
	def withdraw(self, amount):
		if self.balance - amount >= 100:
			self.balance -= amount
			print('Thank you {}. Your remaining balance is {}.'.format(self.acc_name, self.balance))
		elif 100 > self.balance - amount >= 0:
			print('Your account would be under the min.')
		else:
			print('Sorry, you don\'t have that much money')
	# }}
# }}






# This block of code tests BankAccount and BankAccountSpecial {{
acc1 = BankAccount(100, 'Katie')
acc2 = BankAccountSpecial(200, 'Chris')
print(acc1)
acc1.withdraw(50)
acc1.withdraw(50)
acc1.withdraw(1)
acc1.deposit(999)
acc2.deposit(1)
acc2.withdraw(200)
# }}
