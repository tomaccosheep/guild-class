pally = input("What is the palindrome you would like to input? ")
if (len(pally) % 2):
	char_check = (len(pally) // 2) + 1
else: char_check = (len(pally) // 2)

print(char_check)

for i in range(char_check):
	print(i)
	if pally[i] == pally[(len(pally) - 1) - i]:
		print('good')
	else: print('bad')
