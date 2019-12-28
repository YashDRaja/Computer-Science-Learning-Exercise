#Name: Yash Raja
#Date: September 22nd. 2017
#File Name: 2.1_#3.py
#Description: Askes the user for two different numbers and then outputs
#the bigger number
#Test Cases: 1 and 2, 2 and 1

number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter a number different then the first one: "))

if number1 > number2:
    print(number1, "is larger than", number2)
else:
    print(number2, "is larger than", number1)
