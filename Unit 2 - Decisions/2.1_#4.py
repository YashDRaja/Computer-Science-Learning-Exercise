#Name: Yash Raja
#Date: September 22nd. 2017
#File Name: 2.1_#4.py
#Description: Askes the user to enter two different numbers then outputs
#the smaller number
#Test Cases: 1 and 2, 2 and 1
number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter a number different then the first one: "))

if number1 < number2:
    print(number1, "is smaller than", number2)
else:
    print(number2, "is smaller than", number1)
