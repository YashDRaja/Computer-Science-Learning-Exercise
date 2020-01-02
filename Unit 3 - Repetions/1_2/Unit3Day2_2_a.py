#Name: Yash Raja
#Date: October 16th, 2017
#File Name: Unit3_Day2_2_a.py
#Description: Reads five marks and computes the average
#Test Cases: 2 and 2.5 and 3.6

markTotal = 0
for i in range (5):
    mark = float(input("Enter the mark in percentage: "))
    markTotal = markTotal + mark

markTotal = (markTotal / 5)
print("The average of the marks are ", markTotal,"%", sep="")
