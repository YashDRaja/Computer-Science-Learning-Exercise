#Name: Yash Raja
#Date: October 2nd, 2017
#File Name: 2.3_Day2_4.py
#Description: Program 2 reads three integer and determine if any of the three
#are a multiple of the other two. Program 1 reads three integers and determines
#if exactly two are greater than 10

integer1 = int(input("Enter an integer: "))
integer2 = int(input("Enter an integer: "))
integer3 = int(input("Enter an integer: "))


if integer1 > 10 and integer2 > 10 and integer3 > 10:
    print("All 3 integers are greater than 10")
elif integer1 > 10 and integer3 > 10:
    print("The first and third integer are greater than 10")
elif integer1 > 10 and integer2 > 10:
    print("The first and second integer are greater than 10")
elif integer2 > 10 and integer3 > 10:
    print("The second and third integer are greater than 10")
else:
    print("Either only 1 integer is greater than 10 or none are")
    

#Program 2

integer1 = int(input("Enter an integer: "))
integer2 = int(input("Enter an integer: "))
integer3 = int(input("Enter an integer: "))

integer1_2 = integer1 % integer2
integer1_3 = integer1 % integer3
integer2_1 = integer2 % integer1
integer2_3 = integer2 % integer3
integer3_1 = integer3 % integer1
integer3_2 = integer3 % integer2

if integer1_2 == 0 and integer1_3 == 0:
    print("The first integer is multiple of second and third integer")
elif integer2_1 == 0 and integer2_3 == 0
    print("The second integer is multiple of first and third integer")
elif integer3_1 == 0 and integer3_2 == 0:
    print("The third integer is multiple of first and second integer")
else:
    print("None of the integers are multiples of the other two")
