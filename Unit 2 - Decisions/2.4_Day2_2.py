#Name: Yash Raja
#Date: October 3rd, 2017
#File Name: 2.4_Day2_2.py
#Description: Asks user if person is doctor, if yes outputs their name with dr.
#if not then asks if male or female and outputs mr. or ms.

personName = input("Enter the persons last name: ")
doctorYesNo = input("If person is doctor, type 'YES'. or if not 'NO', without '': ")
gender = input("If person is female, type 'F', if person is male type 'M', without '': ")

if doctorYesNo == "YES":
    print("Dr.", personName, sep="")
elif doctorYesNo == "NO":
    if gender == "F":
        print("Ms.", personName, sep="")
    if gender == "M":
        print("Mr.", personName, sep="")
    else:
        print("Put a proper gender and try again.")
else:
    print("Answer whether person is doctor or not again and try again.")
