#Name: Yash Raja
#Date: October 24th, 2017
#File Name: 3_2_2_3.py
#Description: Asks user for a word and how many times is should be repeated and then modifies to put sentinel
#Test Cases: go, and , bob, cya

num = 0
word = ""
termination = input("Enter the word that should be entered to end the program: ")

while word != termination:
    print(word*num)
    num = int(input("Enter how many times the the words should be repeated, in positive integers: "))
    word = input("Enter the word that to be repeated, write done to finish program: ")

