#Name: Yash Raja
#Date: 11/2/2017
#File Name: 5_1.py
#Description:Program calculates the sum of the first n integers
#Test Cases: 10, 2, 3, 4, 5, 6, 7, 8, -1, 0
sum = 0
while True:
    try:
        number = int(input("Enter number: "))
        if number < 0:
            letter = int("l")
        break
    except:
        print("Please enter a positive integer greater than 0!")
number += 1
for z in range (number):
    sum += z
number -= 1
print("The sum of the first", number, "integers is", sum)
