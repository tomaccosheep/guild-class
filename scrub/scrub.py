#>>> ms_clean('Readability counts')
#'R9y c4s'
#>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
#'Errors should never pass silently.'
import re
def scrub_numbers(raw_data: str) -> str:
	return re.sub(r'\d', '', raw_data)

def gentle_clean(raw_data: str) -> str:
	return re.sub('\s?[-_]', ' ', raw_data)

def clean_data(raw_data: str) -> str:
	a = re.sub('[\-,_]', ' ', raw_data)
	print(a)
	return re.sub('[\s,]{2,}|[\d]', '', a)
def some_scrubber(raw_data: str) -> str:
	a = re.sub('(?<=[A-Z]|[a-z]|\.)\s', '', raw_data)
	return re.sub('\s{2}', ' ', a)
def mr_clean(raw_data: str) -> str:
	return re.sub('(?<=[A-Z]|[a-z]|\s)', ' ', raw_data)
def ms_clean(raw_data: str) -> str:
	out = ''
	relist = re.split('(?<=[A-Z]|[a-z]).(?=[A-Z]|[a-z])', raw_data)
	print(relist)
	out += str(relist[0])
	print(out)
	count = 0
	for i in range(1, len(relist)):
		if relist[i] != '' and relist[i-1] != '':
			out += ' '	
			out += relist[i]
			print(out)
		if relist[i] == '' and relist[i-1] != '':
			count += 1
		if relist[i] == '' and relist[i-1] == '':
			count += 1
		if relist[i] != '' and relist[i-1] == '':
			count += 1
			out += str(count)
			out += str(relist[i])
			count = 0
	return out
def strong_cleaner(raw_data: str) -> str:
	a = re.sub('[@,#,%,$,\d,*,&,!,(]', '', raw_data)
	return re.sub('(?<=[A-Z]|[a-z])[A-Z]', '', a)
def extracto(raw_data: str) -> int:
	iterator = 0
	relist = re.split('.', raw_data)
	print(relist)
	for i in relist:
		try:
			i2 = int(i)
			iterator += i2
		except:
			continue
	return iterator
