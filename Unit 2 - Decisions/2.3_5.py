#Name: Yash Raja
#Date: October 1st, 2017
#File Name: 2.3_5.py
#Description: Program #1 - Prints message if user enters an A, regardless of
#case. Program #2 - Determines if given integer is divisble by either 3 or 5.
# Program #3 - Determine if a given integer is divisble by both 3 and 5,
# Program #4 - Determine if a given integer is not a multiple of 4 and 7
# Program #5 - Determine if two given integers are both positive, both
# negative, or one positive and negative

#Program 1
letter = input("Please enter a letter: ")

if letter == "a" or letter == "A":
    print("The letter you inputed is 'a' or 'A' ")
else:
    print("The letter is neither 'a' or 'A'")
#Program 2
integer = int(input("Please enter an integer: "))
integerDiv3 = integer % 3
integerDiv5 = integer % 5

if integerDiv3 == 0 or integerDiv5 == 0:
    print("The number is divisible by 3 or 5 or by both.")
else:
    print("The number is divisible by neither 3 or 5")

#Program 3
integer0 = int(input("Please enter an integer: "))
integerDiv13 = integer0 % 3
integerDiv15 = integer0 % 5

if integerDiv13 == 0 and integerDiv15 == 0:
    print("The number is divisible by 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5")
#Program 4
integer = int(input("Please enter an integer: "))
integerMultiple4 = integer % 4
integerMultiple7 = integer % 7

if not(integerMultiple4 == 0) or not(integerMultiple7 == 0):
    print("The number is not a multiple of 4 or 7")
else:
    print("The number is a multiple of neither 4 or 7")
#Program 5
integer1 = int(input("Please enter a integer it can be negative or positive: "))
integer2 = int(input("Please enter a integer it can be negative or positive: "))

if integer1 < 0 and integer2 < 0:
    print("Both integers are negative")
elif integer1 > 0 and integer2 > 0:
    print("Both integers are positive")
elif integer1 < 0 and integer2 > 0:
    print("The first integer is negative and the second integer is positive")
elif integer1 > 0 and integer2 < 0:
    print("The first integer is positive and the second integer is negative")
