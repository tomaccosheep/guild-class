import random


# Create a 'card' object
# The object should have suit_num(0-3, alphabetical), rank_num(1-13), value, suit(string), rank(string)
# {{
class Card(object):
	def __init__(self, suit_num, rank_num):
		# Organize infor based on suit number, rank number {{
		self.suit_num = suit_num
		self.rank_num = rank_num
		if self.rank_num == 0:
			self.rank = 'ace'
		elif self.rank_num > 10:
			self.value = 10
			if self.rank_num == 11:
				self.rank = 'jack'
			elif self.rank_num == 12:
				self.rank = 'queen'
			elif self.rank_num == 13:
				self.rank = 'king'
			else:
				return ValueError
		else:
			self.value = rank_num
			self.rank = str(self.rank_num)
		# }}

		# Make suit strings out of suit numbers {{
		if suit_num == 0:
			self.suit = 'clubs'
		elif suit_num == 1:
			self.suit = 'diamonds'
		elif suit_num == 2:
			self.suit = 'hearts'
		elif suit_num == 3:
			self.suit = 'spades'
		else:
			return ValueError
		# }}

	def __str__(self):
		return "The {} of {}.".format(self.rank, self.suit)
# }}



# This should be a full set of cards. I can remove cards into a hand, and then into a discard pile.
# {{
class Deck(object):
	# Build a deck of 4 sets of 13, and build an empty discard pile {{
	def __init__(self):
		self._mydeck = []
		self._mydiscard = []
		for i in range(0,4):
			for j in range(1,14):
				self._mydeck.append(Card(i,j))
		for i in range(52):
			print(len(self._mydeck))
			print(self._mydeck[i])
	# }}


	# Return the deck as a list {{
	def __str__(self):
		return self._mydeck
	# }}
	

	# Shuffles the deck {{
	def shuffle(self):
		random.shuffle(self._mydeck)
		return
	# }}

	# Cuts the deck {{
	def cut(self, num):
		tempdeck = []
		tempdeck.extend(self._mydeck[num, 52])
		tempdeck.extend(self._mydeck[0, num])
		self._mydeck = tempdeck
		return
	# }}
	# Draws one card from the list {{
	def draw_one(self):
		return self._mydeck[0].pop
	# }}
	# Puts the inputed card into the discard pile {{
	def discard_one(self, mycard):
		self.mydeck.append(mycard)
		return
	# }}
	# Adds the discard pile back into the deck, and reshuffles it {{
	def shuffle_discard(self):
		self._mydeck.extend(self._mydiscard)
		random.shuffle(self._mydeck)
	# }}
# }}





# Cards collected from the deck.
# {{
class Hand(object):
	def __init__(self):
		self.my_hand = []
		return
	def __str__(self):
		return
	def draw_one(self, my_card):
		self.my_hand.append(my_card):
		return
	def show_hand(self):
		return self.my_hand
	#def 
# }}


#In the game module, implement top-level functions that:
#Start a new game of Blackjack, or Quit
#Score a hand
#Bust if the score is over 21
#Advanced
#Bring in your dealer hitting logic from the 21 practice problem into a top-level function it's own module dealer. Update it to take in a Hand instance and return whether to hit.
#Add a "card counting assistant" function in a module advisor. Have it take in a deck and a hand and print out the probability that you will bust. You can find the expectation value of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.
#Add in a UI so a single user can play versus the dealer.
#Allow multiple hands to be played with the same deck.
