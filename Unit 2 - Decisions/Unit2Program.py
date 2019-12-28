#Name: Yash Raja
#Date: October 12th, 2017
#File Name: Unit2Program.py
#Description: This program checks if a integer is positive, if negative
#then spits out error message. If not negative or 0 then prints out how
#many of each coin
#Test Cases: 169 and 149, 67, and 53, and 26, 5, 9, 19, 2657

numOfPen = int(input("Enter the number of pennies: "))

if numOfPen <0:
    print("Sorry, you need to enter a positive integer to use this program, or not 0")
#Including all 4
elif numOfPen >= 100:
    numOfLoo = numOfPen // 100
    numOfPenMinusLoo = numOfPen - (numOfLoo*100)
    if numOfLoo > 1:
        print(numOfLoo, "loonies")
    else:
        print(numOfLoo, "loonie")
    if numOfPenMinusLoo >= 25:
        numOfQua = numOfPenMinusLoo // 25
        numOfPenMinusQuaAndLoo = numOfPenMinusLoo - (numOfQua*25)
        if numOfQua > 1:
            print(numOfQua, "quarters")
        else:
            print(numOfQua, "quarter")
    else:
        numOfPenMinusQuaAndLoo = numOfPenMinusLoo
    if numOfPenMinusQuaAndLoo >= 10:
        numOfDim = numOfPenMinusQuaAndLoo // 10
        numOfPenMinusDimAndQuaAndLoo = numOfPenMinusQuaAndLoo - (numOfDim*10)
        if numOfDim > 1:
            print(numOfDim, "dimes")
        else:
            print(numOfDim, "dime")
    else:
        numOfPenMinusDimAndQuaAndLoo = numOfPenMinusQuaAndLoo
    if numOfPenMinusDimAndQuaAndLoo >= 1:
        numOfPen = numOfPenMinusDimAndQuaAndLoo // 1
        numOfPenMinusPenAndDimAndQuaAndLoo = numOfPenMinusDimAndQuaAndLoo - (numOfPen*1)
        if numOfPen > 1:
            print(numOfPen, "pennies")
        else:
            print(numOfPen, "pennie")
            
#Including Quarters, Dimes, and Pennies
            
elif numOfPen >= 25:
    numOfQua = numOfPen // 25
    numOfPenMinusQua = numOfPen - (numOfQua*25)
    if numOfQua > 1:
            print(numOfQua, "quarters")
    else:
            print(numOfQua, "quarter")
    if numOfPenMinusQua >= 10:
        numOfDim = numOfPenMinusQua // 10
        numOfPenMinusDimAndQua = numOfPenMinusQua - (numOfDim*10)
        if numOfDim > 1:
            print(numOfDim, "dimes")
        else:
            print(numOfDim, "dime")
    else:
        numOfPenMinusDimAndQua = numOfPenMinusQua
    if numOfPenMinusDimAndQua >= 1:
        numOfPen = numOfPenMinusDimAndQua // 1
        numOfPenMinusPenAndDimAndQua = numOfPenMinusDimAndQua - (numOfPen*1)
    if numOfPen > 1:
        print(numOfPen, "pennies")
    else:
        print(numOfPen, "pennie")
        
#Including Dimes and Pennies
        
elif numOfPen >= 10:
    numOfDim = numOfPen // 10
    numOfPenMinusDim = numOfPen - (numOfDim*10)
    if numOfDim > 1:
        print(numOfDim, "dimes")
    else:
        print(numOfDim, "dime")
    if numOfPenMinusDim >= 1:
        numOfPen = numOfPenMinusDim // 1
        numOfPenMinusPenAndDim = numOfPenMinusDim - (numOfPen*1)
    if numOfPen > 1:
        print(numOfPen, "pennies")
    else:
        print(numOfPen, "pennie")
        
#Including Just Pennies
        
else:
    if numOfPen > 1:
        print(numOfPen, "pennies")
    else:
        print(numOfPen, "pennie")
