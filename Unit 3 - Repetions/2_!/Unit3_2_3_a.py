#Name: Yash Raja
#Date: October 23rd, 2017
#File Name: Unit3_2_3_a.py
#Description: This program asks user for their name and if it is Tim prints you are allowed to enter
#Test Cases: yash , bob, tim, Tim, Yash

name = input("Please enter your name: ")

while (name != "Tim" and name != "tim"):
    print("You are not Tim or Yash!")
    name = input("Please enter your name again: ")
   
if name == "Tim" or name == "tim":
    print("You are allowed to enter")
