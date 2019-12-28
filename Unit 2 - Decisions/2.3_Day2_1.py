#Name: Yash Raja
#Date: October 2nd, 2017
#File Name: 2.3_Day_2_1.py
#Description: Asks user for checkings account balance and savings account
#balance and then outputs a $.15 charge if user does not have 10,000 in checking
#account or doesnt have $15,000 in saving account, or outputs saying no charge

checkingsAccount = float(input("Please enter your checking account balance: "))
savingsAccount = float(input("Please enter your savings account balance: "))

if checkingsAccount >= 10000 or savingsAccount >= 15000:
    print("There is no service charge per check")
else:
    print("There is a service charge of $0.15 per check")
