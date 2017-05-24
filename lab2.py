ugly_number = str(input('What is your phone number? '))
while len(ugly_number) != 10:
	ugly_number = str(input('What is your ten-digit phone number? '))

print(ugly_number[0:3], "-", ugly_number[3:6], "-", ugly_number[6:11])
