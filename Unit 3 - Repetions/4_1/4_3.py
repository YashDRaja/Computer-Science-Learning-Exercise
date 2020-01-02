#Name: Yash Raja
#Date: October 31st, 2017
#File Name: 4_3.py
#Description
#Test Cases:
import random

heads = 0
tails = 0

for z in range (20):
    choice = random.choice("HT")
    if choice == "H":
        heads += 1
        print("H")
    if choice == "T":
        tails += 1
        print("T")
print("The amount of heads flipped are", heads)
