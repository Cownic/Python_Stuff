'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
'''

import random

rn = random.randint(1,9)

print(rn)

print("Random Number generated, user please try to guess...\n")

user_input = input("User guess")

while int(user_input) != rn:
    user_input = input("Wrong Guess, Try again...\n")

print("Congrat!, You manage to guess the random number {}".format(rn))