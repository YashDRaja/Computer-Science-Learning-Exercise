#Name: Yash Raja
#Date: October 3rd, 2017
import math

a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))

d = (b**2) - (4*a*c)

sol1 = (-b+math.sqrt(d))/(2*a)
sol2 = (-b-math.sqrt(d))/(2*a)

if d > 0:
    print("There are two solutions")
    print("The first solution is", sol1)
    print("The second solution is", sol2)
if d < 0:
    print("There is 0 possible real answers")
if d == 0:
    print("There is 1 possible answer")
    print("The solution for x is 0")
