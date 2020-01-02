#Name: Yash Raja
#Date: October 16th, 2017
#File Name: Unit3_Day2_2_b.py
#Description: Reads five marks and computes the average, modified
#to ask user for amount of marks
#Test Cases: 2 and 2.5 and 3.6

numOfMarks = int(input("Enter the amount of marks there are: "))
markTotal = 0
for i in range (numOfMarks):
    mark = float(input("Enter the mark in percentage: "))
    markTotal = markTotal + mark

markTotal = (markTotal / numOfMarks)
print("The average of the marks are ", markTotal,"%", sep="")
