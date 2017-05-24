money_string = input("How much money do you have? Please use $0.00 \
format: ")

if money_string[0] == "$":
	money_num = int(float(money_string[1:]) * 100)
else: money_num = int(float(money_string) * 100)

register = {}

register['dollars'] = int(input("How many dollars are in the register? "))
register['quarters'] = int(input("How many quarters are in the register? "))
register['dimes'] = int(input("How many dimes are in the register? "))
register['nickels'] = int(input("How many nickels are in the register? "))
register['pennies'] = int(input("How many pennies are in the register? "))


dollar = 0
while register['dollars'] > 0 and (money_num // 100) > 0:
	money_num -= 100
	register['dollars'] -= 1
	dollar += 1


quarter = 0
while register['quarters'] > 0 and (money_num // 25) > 0:
	money_num -= 25
	register['quarters'] -= 1
	quarter += 1


dime = 0
while register['dimes'] > 0 and (money_num // 10) > 0:
	money_num -= 10
	register['dimes'] -= 1
	dime += 1


nickel = 0
while register['nickels'] > 0 and (money_num // 5) > 0:
	money_num -= 5
	register['nickels'] -= 1
	nickel += 1


penny = 0
while register['pennies'] > 0 and (money_num // 1) > 0:
	money_num -= 1
	register['pennies'] -= 1
	penny += 1

if money_num > 0: print("I can't give you change!")
else:
	print('Dollars: ', dollar,'\nQuarters: ', quarter,'\nDimes: ', dime,'\nNickels: ', nickel,'\nPennies: ', penny)
