#Name: Yash Raja
#Date: November 6th, 2017
#File Name: 3.6.1.py
#Description includes all answers and programs of 3.6
#Question 1
"""
        *
       ***
      *****
     *******
    *********
   ***********
  *************
"""

#Question 2a
for i in range (1,4):
    print(("++++"))
    for z in range(1,4):
        print(("----"))
#Question 2b
for z in range (1,4):
    print("*")
    for b in range (1):
        print("***")
        for i in range (1):
            print("*****")
            for b in range (1):
                print("***")
                for z in range (1):
                    print("*")
#Question 2c
z = 1
m = 1
c = 1
amount = 2
for j in range (3):
    for x in range(amount):
        print("*"*z)
        z += 2
    """for x in range(2):
        print("*"*m)
        m += 2
    for  x in range(2):
        print("*"*c)
        c += 2"""
    amount +=1
    z = 1

#Question 3a i

total = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        if die1 + die2 >= 9:
            total += 1
            print(die1, die2)
print("There are", total, "possible rolls that sum to 9.")

#Question 3a ii

total = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        if die1 + die2 % 3 != 0 or die1 + die2 % 5 != 0:
            total += 1
            print(die1, die2)
print("There are", total, "possible rolls that are not divisble by 3 or 5.")

#Question 3b i

total = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        for die3 in range (1,7):
            if die1 + die2 + die3 < 12:
                total += 1
                print(die1, die2, die3)
print("There are", total, "possible rolls that are less than 12")

#Question 3b ii

total = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        for die3 in range(1,7):
            if die1 + die2 + die3 < 11 and die1 + die2 + die3 > 7:
                total += 1
                print(die1, die2,3)
print("There are", total, "possible rolls that are between 7 and 11")

#Question 3b iii

total = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        if die1 + die2 + die3 == 3 or die1 + die2 + die3 == 5 or die1 + die2 + die3 == 7 or die1 + die2 + die3 == 11 or die1 + die2 + die3 == 13 or die1 + die2 + die3 == 17 :
            total += 1
            print(die1, die2, die3)
print("There are", total, "possible rolls that is a prime number")

#Question 4

num = int(input("Enter number: "))

for z in range(1,num + 2, 2):
    print("*"*z)
for x in range(num-2, 0, -2):
    print("*"*x)
