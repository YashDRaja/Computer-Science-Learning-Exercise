#Name: Yash Raja
#Date: October 24rd, 2017
#File Name: 3_2_2_2.py
#Description: Asks user for integer, then squares the integer, and adds it to the other squares of the other integers
#If user enters negative calculate the sum of squares up until that point and then ends
#Test Cases: 10 and 15 and 25 and -1, -1

n = int(input("Enter integers, for the program to square and add: "))
p = 0

while n >= 0:
    n = n**2
    p += n
    n = int(input("Enter integers, for the program to square and add: "))
print(p,"is the value of all the positive inputs squared and added")    
