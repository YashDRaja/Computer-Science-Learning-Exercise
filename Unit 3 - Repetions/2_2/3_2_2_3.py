#Name: Yash Raja
#Date: October 24rd, 2017
#File Name: 3_2_2_3.py
#Description: Asks user for integers and outputs highest 2
#Test Cases: 3 and 5 and 7 and 10 and 12 and 1111 and 1000 and -2, 100 and 112 and 251 and -2

n = int(input("Enter integer: "))
p = 0
integerHigh = 0
integerSec = 0

while n > 0:
    if n > integerSec:
        if n > integerHigh:
            integerSec = integerHigh
            integerHigh = n
        else:
            integerSec = n
    n = int(input("Enter integer: "))
    
print("The values of two highest integers in order are,", integerHigh, "and", integerSec)    
