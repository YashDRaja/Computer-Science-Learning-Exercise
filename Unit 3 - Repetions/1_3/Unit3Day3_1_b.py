#Name: Yash Raja
#Date: October 19th, 2017
#File Name: Unit3_Day3_b.py
#Description: Asks user for integer between 1 and 50 and then outputs all factor
#if number is prime says so
#Test Cases:

num = int(input("Enter an integer between 1 and 50: "))
n = 0
z = 0
number = 1 + num
if num > 1 and num < 50:
    print("The factors of", num, "are:")
    for x in range (0,number):
        n = n + 1
        if num % n == 0:
            z = z + 1
            print(n)
else:
    print("Incorrect input")
if z == 2:
    print("The number is prime")
