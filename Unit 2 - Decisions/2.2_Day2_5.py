#Name: Yash Raja
#Date: October 1st, 2017

hoursWorked = int(input("Please enter the amount of hours you worked, in positive integer amount: "))
hoursWorked40 = hoursWorked*12.00

if hoursWorked >= 0:
    if hoursWorked <= 40:
        hoursWorked40 = hoursWorked*12.00
        print("You earned $", hoursWorked40 , sep="")

    elif hoursWorked > 40:
        hoursWorked = hoursWorked - 40
        hoursWorkedCost = (hoursWorked * 15) + (40 * 12)
        print("You earned $", hoursWorkedCost, sep="")
else:
    print("Enter a positive number")
