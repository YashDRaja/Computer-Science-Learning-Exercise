#Name: Yash Raja
#Date: October 27th, 2017
#File Name: 4_2_b.py
#Description: Generate a random tax rate between 10 and 20%
#then calculate the tax on an item whose price is determined by the user.
#Test Cases: 15

import random

price = float(input("What is the price of the product: "))
f = 0
f = random.randint(10,20)
f = f / 100
f += 1
f *= price
f = round(f, 3)
print("It will cost $", f)
