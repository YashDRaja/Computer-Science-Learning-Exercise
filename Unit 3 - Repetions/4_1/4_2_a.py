#Name: Yash Raja
#Date: October 27th, 2017
#File Name: 4_2_a.py
#Description: Generate a random floating-point value f such that 5 ≤ f < 15.
#Test Cases: None because it doesnt have input

import random

f = 0

while not(f >= 5 and f < 15):
    f = 15*random.random()

print("You got", f)
