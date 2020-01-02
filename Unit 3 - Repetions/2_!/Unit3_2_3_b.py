#Name: Yash Raja
#Date: October 23rd, 2017
#File Name: Unit3_2_3_b.py
#Description: This program asks user for their name and if it is Yash or Tim prints you are allowed to enter
#Test Cases: yash , bob, tim, Tim, Yash

name = input("Please enter your name: ")

while (name != "Tim" and name != "tim") and (name != "Yash" and name != "yash"):
    print("You are not Tim or Yash!")
    name = input("Please enter your name again: ")

if name == "Tim" or name == "tim" or name == "Yash" or name == "yash":
    print("You are allowed to enter")
