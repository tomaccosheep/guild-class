#Card class with a suit and a rank Deck class with a collection of cards Hand class with a collection of cards from a deck.
#In the deck module, implement methods that:
#
#Return a shuffled deck
#Cut the deck
#Draw a card off the top of a deck
#In the hand module, implement methods that:
#
#Add a card to a hand
#Allow a user to type in a hand and have it be converted into a Hand object
#In the game module, implement top-level functions that:
#
#Start a new game of Blackjack, or Quit
#Score a hand
#Bust if the score is over 21
#Scoring
#
#Cards have integer point values. Aces are 1 or 11, number cards are their number, face cards are all 10. A hand is worth the sum of all the points of the cards in it. An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
#
#Advanced
#
#Bring in your dealer hitting logic from the 21 practice problem into a top-level function it's own module dealer. Update it to take in a Hand instance and return whether to hit.
#
#Add a "card counting assistant" function in a module advisor. Have it take in a deck and a hand and print out the probability that you will bust. You can find the expectation value of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.
#
#Add in a UI so a single user can play versus the dealer.
#
#Allow multiple hands to be played with the same deck.

import random


# Create a 'card' object
# The object should have suit_num(0-3, alphabetical), rank_num(1-13), value, suit(string), rank(string)
# {{
class Card(object):
	def __init__(self, suit_num, rank_num):
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

	def __str__(self):
		return "The {} of {}.".format(self.rank, self.suit)
# }}

# This should be a full set of cards. I can remove cards into a hand, and then into a discard pile.
# {{
class Deck(object):
	def __init__(self):
		self._mydeck = []
		for i in range(0,4):
			for j in range(1,14):
				self._mydeck.append(Card(i,j))
		for i in range(52):
			print(len(self._mydeck))
			print(self._mydeck[i])
	def __str__(self):
		for i in range(0,52):
			print(self._mydeck[i])
		return str(self._mydeck[0])
	def shuffle(self):
		random.shuffle(self._mydeck)
		return
	def cut(self, num):
		tempdeck = []
		tempdeck.append(self._mydeck[num, 52])
		tempdeck.append(self._mydeck[0, num])
		self._mydeck = tempdeck
		return
# }}

# Cards collected from the deck.
# {{
class Hand(object):
	def __init__(self):
		return
# }}
