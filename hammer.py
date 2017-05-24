time = str(input('What time is it? Please write in \'0:00 AM\' format: '))
	
if time[1] == ':':
	col = 1
elif time [2] == ':':
	col = 2

if col == 1:
	time_num = float(time[0])
elif col == 2:
	time_num = float((int(time[0]) * 10) + int(time[1]))
	print(time_num)

if time[0:2] == '12':
	if str.lower(time[-2]) == 'a':
		time_num = time_num - 12	
elif str.lower(time[-2]) == 'p':
	time_num = time_num + 12


time_num = time_num + (int(time[col + 1]) * 10 + int(time[col + 2])) / 60

if time_num >= 7 and time_num <=9:
	print(time_num)
	print("It's breakfast time!")
elif time_num >= 12 and time_num <=14:
	print(time_num)
	print("It's lunch time!")
elif time_num >= 19 and time_num <=21:
	print(time_num)
	print("It's dinner time!")
elif time_num >= 22 or time_num <=4:
	print(time_num)
	print("It's hammer time!")
else: print ("It must be snack time!")
