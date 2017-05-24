eword = input('What is the e-word? ')
if "ei" in eword.lower():
	index = eword.find('ei')
	if eword[index-1].lower() == 'c':
		print('This follows the rule. After \'c\', \'i\' does not come before \'e\'')
	else: print('This breaks the rule. \'i\' should come before \'e.\'')
if "ie" in eword.lower():
	index = eword.find('ie')
	if eword[index-1].lower() == 'c':
		print('This breaks the rule. After \'c\' \'i\' should not come before \'e\'')
	else: print('This follows the rule. There is no \'c\' to follow, so \'i\' comes before \'e.\'')
