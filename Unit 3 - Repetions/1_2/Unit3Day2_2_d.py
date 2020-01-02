#Name: Yash Raja
#Date: October 16th, 2017
#File Name: Unit3_Day2_2_d.py
#Description: Reads five marks and computes the average, modified
#to ask user for amount of marks, and and sees if both numbers are within 100, with error check
#Test Cases: 2 and 2.5 and 3.6

numOfMarks = int(input("Enter the amount of marks there are: "))
markTotal = 0
markLow = 100
markHigh = 0
num = 0
for i in range (numOfMarks):
    mark = float(input("Enter the mark in percentage: "))
    if mark >= 0 and mark <= 100:
        markTotal += mark
        if mark < markLow:
            markLow = mark
        if mark > markHigh:
            markHigh = mark 
    else:
        print("You entered a mark that is not in 0 and 100")
        num = num + 1
    

markTotal = (markTotal / (numOfMarks - num))
print("The average of the marks are ", markTotal,"%", sep="")
print("The lowest mark is ", markLow, ".", " The highest mark is ", markHigh, ".", sep="")
