import random

# Create a 'card' object
# The object should have suit_num(0-3, alphabetical), rank_num(1-13), value, suit(string), rank(string)
# {{
class Card(object):
	def __init__(self, suit_num, rank_num):



		# Organize information based on suit number, rank number {{
		self.suit_num = suit_num
		self.rank_num = rank_num
		if self.rank_num == 1:
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
			print(self._mydeck[i])
	# }}


	# Return the deck as a list {{
	def __str__(self):
		deckstring = ''
		for i in self._mydeck:
			deckstring += str(i)
		return deckstring
	# }}
	

	# Shuffles the deck {{
	def shuffle(self):
		random.shuffle(self._mydeck)
		return 'Shuffled!'
	# }}


	# Cuts the deck {{
	def cut(self, num):
		tempdeck = []
		tempdeck.extend(self._mydeck[num: 52])
		tempdeck.extend(self._mydeck[0: num])
		self._mydeck = tempdeck
		return
	# }}



	# Draws one card from the list {{
	def draw_one(self):
		return self._mydeck.pop(0)
	# }}



	# Puts the inputed card into the discard pile {{
	def discard_one(self, mycard):
		self._mydiscard.append(mycard)
		return
	# }}



	# Adds the discard pile back into the deck, and reshuffles it {{
	def shuffle_discard(self):
		self._mydeck.extend(self._mydiscard)
		random.shuffle(self._mydeck)
		self._mydiscard = []
	# }}


	# Prints the deck {{
	def print_deck(self):
		for i in self._mydeck:
			print(str(i))
	# }}


	# Prints one specific card {{
	def print_card(self, card_num):
		print(str(self._mydeck[card_num]))
	# }}


	# Prints the discard pile {{
	def print_discard(self):
		for i in self._mydiscard:
			print(str(i))

# }}





# Cards collected from the deck.
# {{
class Hand(object):
	
	# Initiates an empty hand {{
	def __init__(self):
		self._my_hand = []
		return
	# }}


	# Outputs a string of card string outputs {{
	def __str__(self):
		self._my_hand_str = ''
		for i in self._my_hand:
			self._my_hand_str += str(i)
		return self._my_hand_str
	# }}


	# Draw one from the deck into the hand {{
	def draw_one(self, my_card):
		self._my_hand.append(my_card)
		return
	# }}


	# Show the full hand {{
	def show_hand(self):
		for i in self._my_hand:
			print(str(i))
	# }}


	# Prints one specific card {{
	def output_card(self, card_num):
		print(str(self._my_hand[card_num]))
	# }}


	# Discard a card {{
	def discard_one(self):
		return self._my_hand.pop(0)
	# }}


	# Discard all cards {{
	def discard_all(self):
		_self.discard = []
		for i in range(len(self._my_hand)):
			_self.discard.append(self._my_hand.pop(i))
		return _self.discard
	# }}
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
