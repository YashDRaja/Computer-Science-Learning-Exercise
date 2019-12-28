#Name: Yash Raja
#Date: September 22nd, 2017
#File Name: 2.1_Day2_4.py
#Description: Asks user for positive integer and says if integer is odd or even
#Test Cases: 1, 2, 3

number = int(input("Please enter a positive integer: "))

numberOddOrEven = number % 2

if numberOddOrEven == 1:
    print("The number is odd")
else:
    print("The number is even")
