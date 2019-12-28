#Name: Yash Raja
#Date: September 28th, 2017

numberOfItems = int(input("Please enter the amount of items: "))
singleItemHeatingTime = float(input("Please enter the amount of time"+\
                                    " for heating a single item in sec: "))

heatingtime1 = singleItemHeatingTime * 1
heatingtime2 = singleItemHeatingTime * 1.5
heatingtime3 = singleItemHeatingTime * 2

if numberOfItems == 1:
    print("The amount of time you need to heat the items is", heatingtime1, "s")
elif numberOfItems == 2:
    print("The amount of time you need to heat the items is", heatingtime2, "s")
elif numberOfItems == 3:
    print("The amount of time you need to heat the items is", heatingtime3, "s")
    
        
    
