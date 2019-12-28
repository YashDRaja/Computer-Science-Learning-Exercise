#Name: Yash Raja
#Date: October 2nd, 2017
#File Name: 2.3_Day2_2.py
#Description: User enters tire pressures. If users rear tires are the same and
#the front tires are same then it is okay, if not the program determines
#where the pressure is incorrect

rightFrontTire = int(input("Enter right front pressure: "))
leftFrontTire = int(input("Enter left front pressure: "))
rightRearTire = int(input("Enter right rear pressure: "))
leftRearTire = int(input("Enter left rear pressure: "))

if rightFrontTire == leftFrontTire and rightRearTire == leftRearTire:
    print("Inflation is Ok.")
elif rightFrontTire == leftFrontTire and rightRearTire != leftRearTire:
    print("Inflation for front is Ok, and rear is not Ok.")
elif rightFrontTire != leftFrontTire and rightRearTire == leftRearTire:
    print("Inflation for rear is Ok, and front is not Ok.")
else:
    print("The inflation is not Ok, for both rear and front.")
