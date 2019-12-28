#Name: Yash Raja
#Date: September 22nd, 2017
#File Name: 2.1_Day2_2.py
#Description: User inputs cost of meal, if meal is more than $4 then add 8% sales
#Test Cases: 4.00, 4.01, 3.99

costOfMeal = float(input("Please enter the cost of meal: "))
TAX = 0.08

if costOfMeal > 4.00:
        costOfMeal = costOfMeal + (costOfMeal * TAX)
        print("Since your meal costs more then $4.00, there will be tax, you must pay $", costOfMeal, sep="")
else:
    print("The cost of meal was under $4.00 so there is no sales tax, you have to pay $", costOfMeal, sep="")
