#Name: Yash Raja
#Date: October 20th, 2017
#File Name: Unit3_Day3_2.py
#Description: Asks user how many numbers of fibonacci sequence are to be outputted
#then outputs the correct amount of numbers in fibonacci sequence
#Test Cases:

amountOfNum = int(input("Enter the how many numbers of the fibonacci sequence you want: "))
if amountOfNum > 0:
    print("The numbers in fibonacci sequence are: ")
    numberOne =  1
    numberTwo = 1
    amountOfNum = amountOfNum
    for x in range(amountOfNum):
        print(numberTwo)
        numberOne = numberTwo - numberOne
        numberTwo = numberOne + numberTwo
else:
    print("The number imputted is negative or is 0 and cannot be used")
