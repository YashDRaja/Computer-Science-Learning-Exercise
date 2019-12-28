#Name: Yash Raja
#Date: October 3rd, 2017
#File Name: 2.4_Day2_3.py
#Description: Determines discount percent for TV, if plasma then 5% of selling price
# If LCD discount is 8% for 30 inch, 10% of selling price for 42 inch

typeOfTv = input("Please enter type of TV, type 'PLASMA' for plasma,",\
                 "and 'LCD' for LCD. Enter without ''.")
sizeOfTv = int(input("Please enter the size of TV in inches, type", \
                     "'30' for 30 inches, and '42' for 42 inches.",\
                     "Enter without ''."))

if typeOfTv == "PLASMA":
    print("The discount percentage is 5% of the selling price.")
if typeOfTv == "LCD":
    if sizeOfTv == 30:
        print("The discount is 8% of selling price for 30 inch model.")
    if sizeOfTv == 42:
        print("The discount is 10% of selling price for 42 inch model")
