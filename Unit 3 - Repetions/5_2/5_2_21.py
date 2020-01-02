#Name: Yash Raja
#Date: 11/02/2017
#File Name: 5_2_21
#Description: Program calculates the average temperature
#Test Cases:- 14.3, 34, -6, Done
n = 0
avg = 0
print("If you input \"Done\", the program will output the average tempurature")
while True:
    try:
        temp = float(input("Enter the temperature: "))
        n += 1
        avg += temp
    except:
        exit = input("If you would like to quit input \"Done\", (This will not go in to the average): ")
        if exit == "Done":
            break
        else:
            print("Please input \"Done\" or a number for the temperature")
average = avg / n
print("The average temperature is", average, "degrees Celsius")
