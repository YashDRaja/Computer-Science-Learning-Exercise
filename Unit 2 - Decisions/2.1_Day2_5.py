#Name: Yash Raja
#Date: September 22nd, 2017
#File Name: 2.1_Day2_5.py
#Description: Asks user for capacity of their gas tank, indication on gas
#gauge in percent, the fuel consumption per 100km and outputs if safe to process
#or to get gas
#Test Cases: 50 and 75 and 9.2

gasTankCapacity = float(input("Enter the capacity of the gas tank, in litres: "))
gasIndication = float(input("Enter the indication of the gas gauge in percent"+\
                            " do not include percent sign: "))
avgGasConsumtion = float(input("Enter the average gas consuption per 100km/L: "))
amountOfGas = (gasTankCapacity * (gasIndication/100)) * (100/avgGasConsumtion)

if amountOfGas < 350:
    print("Get Gas")
else:
    print("Safe to Proceed")
