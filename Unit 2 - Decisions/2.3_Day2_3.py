#Name: Yash Raja
#Date: October 2nd, 2017
#File Name: 2.3_Day2_3.py
#Description: Asks user for amount of cookie boxes and how many types
#if user order 5 boxes of 1 type he gets 10% of or if he has 10 total boxes
#he also gets 10%, if he has less then that outputs total. Total includes tax

boxesOfCookies = int(input("Enter amount of boxes of cookies you want per type: "))
typeOfCookie = int(input("Enter amount of types, up to 3: "))
totalBoxes = boxesOfCookies * typeOfCookie
costOfCookies = totalBoxes *  6.95

if boxesOfCookies == 5 or totalBoxes == 10:
    costOfCookies90 = costOfCookies * .9
    costOfCookies90 = costOfCookies90 * 1.13
    print("It costs $", costOfCookies90, "for you to get cookies.")
else:
    costOfCookies = costOfCookies * 1.13
    print("It costs you $", costOfCookies, "for you to get cookies")
