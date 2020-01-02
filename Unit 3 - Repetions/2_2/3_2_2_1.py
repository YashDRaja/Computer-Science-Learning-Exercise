#Name: Yash Raja
#Date: October 24rd, 2017
#File Name: 3_2_2_1.py
#Description: Makes user enter as many strings as they like, if quit is inputted
#then stops loop, if it is anything else prints it to screen
#Test Cases:hi, my , name , quit

string = ""
while string != "quit":
    print(string)
    string = input("Enter how many strings you want, to leave input quit: ")
print("Goodbye!")    
