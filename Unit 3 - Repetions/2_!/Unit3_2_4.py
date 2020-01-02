#Name: Yash Raja
#Date: October 23rd, 2017
#File Name: Unit3_2_4
#Description: A problem that asks user a problem continusely until they solve it
#Test Cases:1, 0, -2, 2

answer = 0
n = 0
while answer != 2:
    answer = int(input("Enter the answer to 1+1, it is an integer: "))
    n += 1
if n == 1:
    print("Good job you answered correctly, Wow it only took you one guess!")
else:
    print("Good job you answered correctly in,", n, "guesses")
