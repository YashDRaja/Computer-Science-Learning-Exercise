#Name: Yash Raja
#Date: October 23rd, 2017
#File Name: Unit3_2_2.py
#Description: The program multiples a given integer by three until it exceeds 10000
#Test Cases: 6, 5, 3, 2, 1, 0, -2

num = int(input("Please enter an integer: "))

while num < 10000 and num > 0:
    num *= 3
    print(num)
if num <= 0:
    print("The number is negative or zero")
