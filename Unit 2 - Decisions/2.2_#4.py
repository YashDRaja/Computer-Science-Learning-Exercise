#Name: Yash Raja
#Date: September 26th. 2017
#File Name: 2.2_#4.py
#Description: Asks user for two numbers and says which one is smaller
#Test Cases: 1 and 2, 2 and 1, 2 and 2

number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter a number: "))

if number1 < number2:
    print(number1, "is smaller than", number2)
elif number1 > number2:
    print(number2, "is smaller than", number1)
else:
    print(number1, "is the same as", number2)
