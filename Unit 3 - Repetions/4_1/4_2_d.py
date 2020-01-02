#Name: Yash Raja
#Date: October 27th, 2017
#File Name: 4_2_c.py
#Description: Generates 3 random letters and checks if exactly two of them are vowels
#Test Cases: 
import random

letters1 = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
letters2 = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
letters3 = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
amount = 0

if letters1 == "A" or letters1 == "E" or letters1 == "I" or letters1 == "O" or letters1 == "U":
    amount += 1
if letters2 == "A" or letters2 == "E" or letters2 == "I" or letters2 == "O" or letters2 == "U":
    amount += 1
if letters3 == "A" or letters3 == "E" or letters3 == "I" or letters3 == "O" or letters3 == "U":
    amount += 1
print(letters1)
print(letters2)
print(letters3)

if amount == 2:
    print("Exactly 2 are vowels")
else:
    print("Either none, 1 or 3 of the letters are variables")
