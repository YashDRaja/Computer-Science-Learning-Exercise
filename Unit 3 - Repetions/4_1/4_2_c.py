#Name: Yash Raja
#Date: October 27th, 2017
#File Name: 4_2_c.py
#Description:Make two random selections from the letters in your name,
#then check if they are the same.
#Test Cases: 

import random
for n in range (2):
    name = "Yash"
    name = random.choice(name)
    if n == 1:
        name1 = name
    else:
        name2 = name
if name1 == name2:
    print("The letters selected are", name1, "and", name2, "are both same")
if name1 != name2:
    print("The letters selected are", name1, "and", name2, "are both different")
