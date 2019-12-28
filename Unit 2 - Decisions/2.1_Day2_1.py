#Name: Yash Raja
#Date: September 22nd, 2017
#FileName: 2.1_Day2.py
#Description: Asks the user for two numbers and adds 5 to value of first number
#if second number is greater than 10
#Test Cases: 10 and 9, 9 and 10

number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter another number: "))

if number2 > 10:
    number1 = number1 + 5
    print("The second number you entered was greater then 10, so the first number you entered is",\
          "increased by 5 which makes", number1)
else:
    print("Nothing happened because the second number you entered is lower then 10")
