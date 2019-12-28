#Name: Yash Raja
#Date: September 22th, 2017
#File Name: 2.1_#2.py
#Description: Asks the user for their name, gives a different message
#depending if they use my name or another name
#Test Cases: Yash Raja, Bob Marley, Joe Swanson

name = input("Please enter your full name: ")
myName = "Yash Raja"

if name == myName:
    print("Hello,", name, "I see that you have the same name as", myName)
else:
    print("Hello,", name, "I see that you have a name different from me")
    
