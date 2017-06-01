import re

# This one replaces numbers with empty strings in an inputed string {{
def scrub_numbers(raw_data: str) -> str:
	return re.sub(r'\d', '', raw_data)
# }}


# This one will look for a _ or a -, and possibly a space, and then replace that with a space {{
def gentle_clean(raw_data: str) -> str:
	return re.sub('\s?[-_]', ' ', raw_data)
# }}

# This one will look for a dash or an underscore, and then replace it with a space {{
def clean_data(raw_data: str) -> str:
	a = re.sub('[\-,_]', ' ', raw_data)
	print(a)
	return re.sub('[\s,]{2,}|[\d]', '', a)
# }}

# This one will look for any space that comes after anything, and delete that space {{
def some_scrubber(raw_data: str) -> str:
	a = re.sub('(?<=[A-Z]|[a-z]|\.)\s', '', raw_data)
	return re.sub('\s{2}', ' ', a)
# }}

# This one will look for any character as a "look before" and then add a space after {{
def mr_clean(raw_data: str) -> str:
	return re.sub('(?<=[A-Z]|[a-z]|\s)', ' ', raw_data)
# }}

# 
#def ms_clean(raw_data: str) -> str:
#	out = ''
#	relist = re.split('(?<=[A-Z]|[a-z]).(?=[A-Z]|[a-z])', raw_data)
#	print(relist)
#	out += str(relist[0])
#	print(out)
#	count = 0
#	for i in range(1, len(relist)):
#		if relist[i] != '' and relist[i-1] != '':
#			out += ' '	
#			out += relist[i]
#			print(out)
#		if relist[i] == '' and relist[i-1] != '':
#			count += 1
#		if relist[i] == '' and relist[i-1] == '':
#			count += 1
#		if relist[i] != '' and relist[i-1] == '':
#			count += 1
#			out += str(count)
#			out += str(relist[i])
#			count = 0
#	return out


# This code sets an empty string, out, sets a counter to zero, sets a
# switch called 'ready_to_start' to 1, and then inputs the entire string
# as a list of characters. {{
def ms_clean(raw_data: str) -> str:
	out = ''
	count = 0
	ready_to_start = 1
	relist = re.findall('.', raw_data)
	for i in range(0, len(relist)):
		print(str(i + 1) + ' of ' + str(len(relist)))
		# This part checks if you're at the end of the list.
		# It either wraps up the text unit or outputs a space {{
		if i + 1 == len(relist):
			if relist[i] != ' ':
				out += str(count)
				count = 0
				out += relist[i]
			else:
				out += ' '
		# }}


		# This part checks if you're in a text unit, but not at the
		# end. If it's the beginning of a text unit, then ready_to_start
		# should be a 1, in which case this will set it to 0 and then
		# output the character onto the string. Otherwise, the counter
		# increases by one and moves on {{
		elif relist[i] != ' ' and relist[i+1] != ' ':
			if ready_to_start == 1:
				ready_to_start = 0
				out += relist[i]
			else:
				count += 1
		# }}

		# This part checks for a space. It outputs a space, and it
		# changes the flag to start a new text unit {{
		elif relist[i] == ' ':
			out += ' '
			ready_to_start = 1
		# }}

		# This part checks for the end of a text unit (this part of the 
		# list is not a space, but the next part is). In this case, the
		# counter is added to the string, the counter is reset so it can
		# count the characters of a new word, and the last character of
		# the text unit is added to the string {{
		elif relist[i] != ' ' and relist[i+1] == ' ': 
			out += str(count)
			count = 0
			out += relist[i]
		# }}
	return out
# }}	


# This code filters out strange characters, and then
# it filters out capital letters that follow another non-space character {{
def strong_cleaner(raw_data: str) -> str:
	a = re.sub('[@,#,%,$,\d,*,&,!,(]', '', raw_data)
	return re.sub('(?<=[A-Z]|[a-z])[A-Z]', '', a)
# }}

# This code returns the sum of all the numbers in the string
# {{
def extracto(raw_data: str) -> int:
	sum_int = 0
	relist = re.findall('\d', raw_data)
	print(relist)
	for i in relist:
		try:
			i2 = int(i)
			sum_int += i2
		except:
			continue
	return iterator
# }}
