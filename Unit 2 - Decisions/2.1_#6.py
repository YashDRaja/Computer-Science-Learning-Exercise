#Name: Yash Raja
#Date: September 22nd. 2017
#File Name: 2.1_#6.py
#Description: Asks user for age and if under 16 says too young too drive
#or outputs you are of legal age to drive
#Test Cases: 12, 16, 18

age = float(input("Please enter your age: "))
legalAge = 16

if age < legalAge:
    print("You're too young drive.")
else:
    print("You are of legal age to drive, you can drive if",\
          "you have a driving license",)
