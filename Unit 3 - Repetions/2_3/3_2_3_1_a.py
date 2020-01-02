#Name: Yash Raja
#Date: October 2th, 2017
#File Name: 3_2_3_1_a.py
#Description: 
#Test Cases:

USERNAME = "Username"
username = ""
PASSWORD = "Password"
password = ""

while username != USERNAME or password != PASSWORD:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username != USERNAME or password != PASSWORD:
        print("You have entered either the wrong password or username or both")

print("You are allowed to enter")
