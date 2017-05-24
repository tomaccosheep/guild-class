from random import randrange

num_of_dice = int(input("How many dice will we roll? "))
dice_sides = int(input("How many sides does each die have? "))
for i in range(num_of_dice):
	print('Die #' + str(i + 1) + ' produces a ' + str(randrange(1, dice_sides + 1)))
