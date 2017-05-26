# search {{ }}
import os
import math

# Declare the ari_scale dictionary {{
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
# }}


# Declare a function to calculate the score {{
def calc_score(sen_count, word_count, char_count):
	return math.ceil(4.17*(char_count/word_count) + .5 * (word_count/sen_count) - 21.43)
# }}



# print a prompt based on files in directory, let the user choose a file
# build a dictionary of filenames and numbers, establish an iterator,
# make a list that will hold filtered filenames {{
choose_file_running = True
while choose_file_running:
	file_choice = {}
	file_choice_i = 0
	file_list = []

	# Make a list of files with '.txt' called file_lits {{

	for i in os.listdir('./'):
		if str(i).find('.txt') != -1:
			file_list.append(i)
			print(str(i).find('.txt'))

	# }}

	# For items in file_list, make them an option in the prompt {{

	for i in file_list:
		file_choice_i +=1
		print(str(file_choice_i) + '. to open ' + i)
		file_choice[file_choice_i] = i
	print('q to quit')

	# }}

	# Try to interpret the user's choice {{

	try:
		chosen_file_num = input(':')
		if chosen_file_num == 'q':
			choose_file_running = False
		chosen_file = file_choice[int(chosen_file_num)]
		print('Opening ' + chosen_file)	
		choose_file_running = False
	except:
		continue

	# }}



# quit if 'q' was selected {{

if chosen_file_num == 'q':
	quit()

# }}

#}}


# Make a list of words, and count words and characters {{
f = open(chosen_file)
wordlist = []
sencount = 0
wordcount = 0
charcount = 0
for i in f.read().split():
	wordlist.append(i)
for i in wordlist:
	# Find punctuation to count sentences {{
	if i.find('.') != -1 or i.find('!') != -1 or i.find('?') != -1:
		sencount += 1
	# }}
	# Remove punctuation from the character count {{
	punct_list = [ '.', ',', '\'', '"', '[', ']', '?', '!', '-', ';', ':' ]
	for j in punct_list:
		if i.find(j) != -1:
			charcount -= i.count(j)
	# }}
	# add 1 to word count and word length to character count {{
	wordcount += 1
	charcount += len(i)
	# }}
# }}


# Calculate score within range {{
score = calc_score(sencount, wordcount, charcount)
if score < 1:
	score = 1
if score > 14:
	score = 14
# }}

# print info {{
print('Sentences:',sencount,'\nWords:', wordcount, '\nCharacters:', charcount)

print('Score:', score)
print('Ages:',ari_scale[score]['ages'])
print('Grade Level:',ari_scale[score]['grade_level'])
# }}


