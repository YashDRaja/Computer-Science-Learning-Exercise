#Name: Yash Raja
#Date: September 21st, 2017
#File Name: 2.1_#1.py
#Description: This program uses the integer input of the user, and says
#if the integer is greater than 50 for part a, other than 12 for part b,
#and whther it is equal to or lower than 10 part c
#Test Cases: 51, 12, 9, 10, 50
integerValue = int(input("Please enter an integer: "))

#a
if integerValue > 50: print("HIGHER")
#b
if integerValue != 12: print("OTHER")
#c
if integerValue > 10:
    print("HIGHER")
else:
    print("LOWER")

