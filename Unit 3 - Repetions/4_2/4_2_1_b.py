#Name: Yash Raja
#Date: October 30th, 2017
#File Name: 4_1_1_b
#Description: Guessing game where you have unlimited guesses, while allowing user to quit program by inputting -1
#Test Cases

import random

# Initialize variables
won = False
numTries = 0

# Computer guesses a number between 1 and 100
numToGuess = random.randint(1, 100)

while not(won):

    # Ask the user for a guess and increment number of guesses
    guess = int(input("If you want to quit input -1. Guess a number between 1 and 100: "))

    # Check to see if the guess is correct. Output result
    if guess == numToGuess or guess == -1:
        won = True
    else:
        if guess < numToGuess:
            print("Your guess was too low!")
        else:
            print("Your guess was too high!")

        print("Try again!!")		
if guess == -1:
    print("You have quit the program")
else:
    print("Yay!!!!  You won!!!")
        	
