case = input('Please type a filename: ')
charnum = []
charcount = -1
for i in case[0:]:
	charcount += 1
	if i.isupper():
		style = "camel"
		charnum.append(charcount)
	if i == "_":
		style = "snake"
		charnum.append(charcount)

print(charnum[::-1])

if style == "camel":
	for i in charnum[::-1]:
		letter = case[i]
		case = case[:i] + "_" + letter.lower() + case[i+1:]
		if case[0] == "_":
			case = case[1:]
	print(case)

elif style == "snake":
	for i in charnum[::-1]:
		letter = case[i + 1]
		case = case[:i] + letter.upper() + case[i+2:]
		case = case[0].upper() + case[1:]
	print(case)
		#get lowercase letter
		#delete lowercase letter and underscore
		#insert uppercase letter

else: print("Input error")
