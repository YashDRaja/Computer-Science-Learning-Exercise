#Name: Yash Raja
#Date: October 30th, 2017
#File Name: 4_1_1_a
#Description: Guessing game where you have unlimited guesses
#Test Cases

import random

# Initialize variables
won = False
numTries = 0

# Computer guesses a number between 1 and 100
numToGuess = random.randint(1, 100)

while not(won):

    # Ask the user for a guess and increment number of guesses
    guess = int(input("Guess a number between 1 and 100: "))

    # Check to see if the guess is correct. Output result
    if guess == numToGuess:
        won = True
    else:
        if guess < numToGuess:
            print("Your guess was too low!")
        else:
            print("Your guess was too high!")

        print("Try again!!")		

if won:
	print("Yay!!!!  You won!!!")
        	
