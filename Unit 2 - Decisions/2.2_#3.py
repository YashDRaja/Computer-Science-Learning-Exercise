#Name: Yash Raja
#Date: September 26th. 2017
#File Name: 2.2_#3,py
#Description: Asks user for two numbers and says which is greater or if they are equal
#Test Cases: 1 and 2, 2 and 1, 2 and 2
number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter another number: "))

if number1 > number2:
    print(number1, "is larger than", number2)
elif number1 < number2:
    print(number2, "is larger than", number1)
else:
    print(number1, "is the same as", number2)
