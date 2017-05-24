from random import randrange
print("It's time for the guess-the-number game!")
print("I'm thinking of a number between 1 and 100.")
answer = randrange(1, 100)
guess = -1
guesses = 0
while guess != answer:
	guesses += 1
	guess = int(input("What is your guess? "))
	if guess < answer:
		print("Too low!")
	if guess > answer:
		print("Too high!")
print("You got it in " + str(guesses) + " guesses!")
