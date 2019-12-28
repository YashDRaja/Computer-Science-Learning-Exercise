#Name: Yash Raja
#Date: September 22nd, 2017
#File Name: 2.1_#5.py
#Description: Asks the user to answer 3 different problems
#and then if the user answers properly says they are correct and if they are wrong
#and shows the correct answer
#Test Cases: 1 and 125 and 10703, and 2 and 124 and 121
questionOne = float(input("Enter the answer to, 1**1000="))
answerOne = float(1**1000)

if questionOne == answerOne:
    print("Good Job! You answered correctly")
else:
    print("Your answer is incorrect, the correct answer was", answerOne)

print()

questionTwo = float(input("Enter the answer to, 5**3="))
answerTwo = float(5**3)

if questionTwo == answerTwo:
    print("Good Job! You answered correctly")
else:
    print("Your answer is incorrect, the correct answer was", answerTwo)

print()

questionThree = float(input("Enter the answer to, 55+22*3="))
answerThree = float(55+22*3)

if questionThree == answerThree:
    print("Good Job! You answered correctly")
else:
    print("Your answer is incorrect, the correct answer was", answerThree)
