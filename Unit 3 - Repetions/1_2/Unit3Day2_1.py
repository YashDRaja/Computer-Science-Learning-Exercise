#Name: Yash Raja
#Date: October 16th, 2017
#File Name: Unit3_Day2_1.py
#Description: The program asks a user how many items were on their grocery bill.
#Then ask the user to enter the cost of each item on the grocery bill. When
#the user is done, output the total cost of their groceries plus HST
#Test Cases: 2 and 2.5 and 3

numOfItems = int(input("Enter the amount of items: "))
costTotal = 0
for i in range (numOfItems):
    cost = float(input("Enter the cost of the item: "))
    costTotal = costTotal + cost

costTotal = (costTotal * 1.13)*100
costTotal = round(costTotal)
costTotal = costTotal / 100
print("The total cost of your groceries are", costTotal)
