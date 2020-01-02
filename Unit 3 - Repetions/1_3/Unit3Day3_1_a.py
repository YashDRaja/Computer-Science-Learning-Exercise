#Name: Yash Raja
#Date: October 19th, 2017
#File Name: Unit3_Day3_a.py
#Description: Asks user for integer between 1 and 50 and then outputs all factor
#Test Cases:

num = int(input("Enter an integer between 1 and 50: "))
n = 0
number = 1 + num
if num > 1 and num < 50:
    print("The factors of", num, "are:")
    for x in range (0,number):
        n = n + 1
        if num % n == 0:
            print(n)
else:
    print("Incorrect input")
