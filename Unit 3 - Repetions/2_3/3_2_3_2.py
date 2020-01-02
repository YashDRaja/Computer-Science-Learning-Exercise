#Name: Yash Raja
#Date: November 8th, 2017
#File Name: 3_2_3_2.py
#Description: Using Collatz conjecture, asks user for number and when it reaches 1 shows many times it took you till you got 1

number = 0
iterations = 0

while number != 1:
    number = int(input("Please enter a number: "))
    if number > 0:
        while number != -1:
            if number != 1 and number % 2 == 0:
                number = number/2
                iterations += 1
            elif number != 1 and number % 2 == 1:
                number = (number*3)+1
                iterations += 1
            print(number)
            if number == 1:
                print("It took you,", iterations, "iterations to get to the number 1")
                break
    else:
        break


