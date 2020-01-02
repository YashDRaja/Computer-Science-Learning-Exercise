'''

integer = int(input("What number do you want this make a time table for: "))
number = 0
for z in range(1,13):
    number = number + 1
    print(number, "x", integer, "=", number*integer)
print("")
number = 11
for z in range(1,11,1):
    number = number - 1
    print(number, "^2 = ", number**2, sep="")
    print(number, "^3 = ", number**3, sep="")

sum = 0
sum = 0
'''
print("This program will add 3 integers")
wins = 0
loses = 0
for i in range (10):
    num = input("Enter result of game (W) or (L): ")
    if num == "W" or num == "w":
         wins = wins + 1
    elif num == "L" or num == "l":
        loses = loses + 1
    else:
        print("The thing you inputted is wrong")

if wins > 1:
    print("You won", wins, "games")
elif wins == 1:
    print("You won", wins, "game")
else:
    print("You won no games")
if loses > 1:
    print("You lost", loses, "games")
elif loses == 1:
    print("You lost", loses, "game")
else:
    print("You lost no games")

