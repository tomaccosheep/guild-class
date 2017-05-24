print("This program will create a mad lib based on your input.")
print("First, you will enter three nouns.")
noun1 = input("Enter a noun: ").capitalize()
noun2 = input("Enter a noun: ").capitalize()
noun3 = input("Enter a noun: ").lower()
print("Next, you will enter four verbs.")
verb1 = input("Enter a verb: ").lower()
verb2 = input("Enter a verb: ").lower()
verb3p = input("Enter a verb (past tense): ").lower()
verb4p = input("Enter a verb (past tense): ").lower()
print("And finally, you will enter three adjectives.")
adj1 = input("Enter an adjective: ").capitalize()
adj2 = input("Enter an adjective: ").lower()
adj3 = input("Enter an adjective: ").lower()


out = "\n\nBeware the {n1}, my son!\nThe jaws that {v1}, the claws that {v2}!\n\
Beware the Jubjub {n2}, and shun\n\
The {a1} Bandersnatch!\n\
He took his vorpal {n3} in hand:\n\
Long time the {a2} foe he sought\n\
So {v3p} he by the {a3} tree,\n\
And {v4p} awhile in thought.".format(n1=noun1, n2=noun2, n3=noun3, v1=verb1,
  v2=verb2, v3p=verb3p, v4p=verb4p, a1=adj1, a2=adj2, a3=adj3)
print(out)
