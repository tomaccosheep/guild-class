import curses
from time import sleep

myscreen = curses.initscr()


myscreen.addstr(4, 10, "0000000")
myscreen.addstr(5, 10, "0000000")
myscreen.addstr(6, 10, "0000000")
myscreen.addstr(7, 10, "0000000")
myscreen.addstr(8, 10, "0000000")
myscreen.addstr(9, 10, "0000000")
myscreen.refresh()

# This part sets up a list of lists that correlates to the screen 
# The seventh list is a list of '-' to stop any falling pieces {{
xlist = []
ylist = []
for i in range(6):
	for j in range(7):
		xlist.append('0')
	ylist.append(xlist)
	xlist = []
for i in range(7):
	xlist.append('-')
ylist.append(xlist)
# }}


# This is a test input
# {{
x_input = 4
y_input = -1
while ylist[y_input + 1][x_input] == '0':
	y_input += 1
	myscreen.addch(y_input + 4, x_input + 10, 'r')
	if y_input > 0:
		myscreen.addch(y_input + 3, x_input + 10, '0')
	myscreen.refresh()
	sleep(.5)
# }}	


myscreen.refresh()
myscreen.getch()

curses.endwin()


print(ylist)
