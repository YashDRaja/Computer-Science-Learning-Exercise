#Name: Yash Raja
#Date: October 3rd, 2017
#File Name: 2.4_Day2_1_A.py
#Description: Program determines smallest of three integers

integer1 = int(input("Enter an integer: "))
integer2 = int(input("Enter an integer: "))
integer3 = int(input("Enter an integer: "))

if integer1 == integer2 or integer2 == integer3 or integer1 == integer3:
    print("Some of the numbers may be the same as other, change this and try again")
elif integer1 < integer2:
    if integer1 < integer3:
        print(integer1, "is the smallest integer.")
    if integer1 > integer3:
        print(integer3, "is the smallest integer.")
elif integer2 < integer3:
    print(integer2, "is the smallest integer.")
else:
    print(integer3, "is the smallest integer.")
