#Name: Yash Raja
#Date: September 22nd, 2017
#File Name: 2.1_Day2_3.py
#Description: Asks user for two integers and then asks for first number
#modulo second number and then compares it to the answer
#Test Cases: 2 and 1 and 0, 5 and 2 and 1, 2 and 2 and 1

num1 = int(input("Please enter the first integer value: "))
num2 = int(input("Please enter the second integer value: "))
userSumOfNum = float(input("Please enter the answer to your first number % the second number: "))
sumOfNum = num1 % num2

if userSumOfNum == sumOfNum:
    print("Congratulations you answered correctly")
else:
    print("Wrong Answer you answered", userSumOfNum, "the correct answer was,", sumOfNum)
