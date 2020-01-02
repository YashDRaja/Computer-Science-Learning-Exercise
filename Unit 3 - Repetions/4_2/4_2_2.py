#Name: Yash Raja
#Date: October 31st, 2017
#File Name: 4_2_2.py
#Description:
#Test Cases:
import random
userinp = "R"
n = 0
w = 0
l = 0
t = 0
userinp2 = "Yes"
while userinp == "Rock" or userinp == "rock" or userinp == "R" or userinp == "Paper" or userinp == "paper" or userinp == "P" or userinp == "Scissors" or userinp == "scissors" or userinp == "S":
    while userinp2 == "Yes":
        compChoice = random.choice("RPS")
        if n >= 1:
            userinp = input("Please enter Rock, Paper or Scissors if anything else is inputted the program will stop: ")
            if compChoice == "R":
                if userinp == "Rock" or userinp == "rock" or userinp == "R":
                    print("Tie, Rock vs Rock")
                    t += 1
                if userinp == "Paper" or userinp == "paper" or userinp == "P":
                    print("Win, Paper beats Rock")
                    w += 1
                if userinp == "Scissors" or userinp == "scissors" or userinp == "S":
                    print("Lose, Scissors loses to Rock")
                    l += 1
            if compChoice == "P":
                if userinp == "Rock" or userinp == "rock" or userinp == "R":
                    print("Lose, Rock loses to Paper")
                    l += 1
                if userinp == "Paper" or userinp == "paper" or userinp == "P":
                    print("Tie, Paper vs Paper")
                    t += 1
                if userinp == "Scissors" or userinp == "scissors" or userinp == "S":
                    print("Wins, Scissors beats Paper")
                    w += 1
            if compChoice == "S":
                if userinp == "Rock" or userinp == "rock" or userinp == "R":
                    print("Win, Rock vs Scissors")
                    l += 1
                if userinp == "Paper" or userinp == "paper" or userinp == "P":
                    print("Lose, Paper loses to Scissors")
                    t += 1
                if userinp == "Scissors" or userinp == "scissors" or userinp == "S":
                    print("Tie, Scissors beats Scissors")
                    w += 1
        if n >= 1:
            userinp2 = input("Please enter \"Yes\" if you would like to play again: ")
        n += 1
        print("-----------------------------------------------")
