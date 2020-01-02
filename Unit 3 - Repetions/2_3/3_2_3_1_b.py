#Name: Yash Raja
#Date: October 2th, 2017
#File Name: 3_2_3_1_c.py
#Description: Program checks user name and password, has multiple users, and has a 10 attempt lock
#Test Cases: Username and Password, user and password, username and password

USERNAME1 = "Username"
USERNAME2 = "username"
USERNAME3 = "user"
username = ""
PASSWORD1 = "Password"
PASSWORD2 = "password"
PASSWORD3 = "pass"
password = ""
n = 0
c = 0
while n == 0 and c <= 10:
    c += 1
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username == USERNAME1 and password == PASSWORD1:
        n += 1
    if username == USERNAME2 and password == PASSWORD2:
        n += 1  
    if username == USERNAME3 and password == PASSWORD3:
        n += 1
    if n == 0:
        print("You have entered the wrong username(s) or password(s) or both")
if c <= 10:
    print("You are allowed to enter")
else:
    print("You have been locked out")
