#from random import randrange
#
#def die(num_dice, num_sides=6, *args, **kwargs):
#	for d in range(num_dice):
#		print(text)
#		print('Die #{} produces {}'.format(d, randrange(1, num_sides + 1)))
#
#
#die(text='hello', num_sides=6, num_dice=10)


#def make_list_of_strings(*args):
#	return ' '.join(list(args))
#
#lst = make_list_of_strings('the', 'cat', 'in', 'the', 'hat')
#
#print(lst)

def flower_colors(**kwargs):
	print(kwargs)

flower_colors(Chrysanthemum='red', Marigold='yellow')
