#Name: Yash Raja
#Date: October 20th, 2017
#File Name: Unit3_Day3_4_c.py
#Description: Prints a hollow rectangle, thats dimensions are determined by the user
#Test Cases:

n = int(input("Enter the height of the rectangle: "))
m = int(input("Enter the width of the rectangle: "))
if m >=2:
    print("*"*m)
    n = n-2
    for z in range (n):
            k = m - 2
            print("*"," "*k,"*", sep="")
print("*"*m)
