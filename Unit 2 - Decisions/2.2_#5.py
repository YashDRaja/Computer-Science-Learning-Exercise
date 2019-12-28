#Name: Yash Raja
#Date: Semptemeber 26th, 2017
#File Name: 2.2_#5.py
#Description: Asks user for an integer and says if number is positive, negative
#or neither
#Test Cases: 2, -1, 0

number = int(input("Please enter an integer: "))

if number > 0:
    print(number, "is a positive number.")
elif number < 0:
    print(number, "is a negative number.")
else:
    print(number, "is neither positive or negative.")
