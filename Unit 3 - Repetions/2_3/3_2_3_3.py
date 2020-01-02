#Name: Yash Raja
#Date: November 0th, 2017
#File Name: 3_2_3_3.py
#Description count the number of sevens
num = int(input("Enter a number: "))
number = 0
while num >= 1:
    digit = num % 10
    num = num//10
    if digit == 7:
        number += 1
print("There are", number, "7's")

#b
num = int(input("Enter a number: "))
even = 0
odd = 0
while num >= 1:
    digit = num % 10
    num = num//10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
print("There are", even, "even numbers and", odd, "odd numbers")

#c
num = int(input("Enter a number: "))
even = 0
odd = 0
sum = 0
while num >= 1:
    digit = num % 10
    num = num//10
    sum += digit
print("The sum of the number is", sum)

