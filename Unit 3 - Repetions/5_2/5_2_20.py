#Name: Yash Raja
#Date: 11/2/2017
#File Name: 5_2_20.py
#Description: User enters grades, when user inputs -1 quit program
#Test Cases: 10, 2, 3, 4, 5, 6, 7, 8, -1, 0
avg = 0
n = 0
mark = 0
number = 0
while number != -1:
    try:
        number = int(input("Enter number, enter -1 to quit the program: "))
        if number != -1:
            n+= 1
            mark += number
    except:
        print("Please enter a mark")
avg = mark/n
print("The avg of your marks is", avg)
