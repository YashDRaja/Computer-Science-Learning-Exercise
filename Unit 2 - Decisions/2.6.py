#Name: Yash Raja
#Date: October 4th, 2017
#File Name: 2.6.py
#Description: Asks user for alien antennae and amount of eyes and outputs the
#aliens it matches

amountOfAntennae = int(input("Enter the amount of antennaes the alien has: "))
amountOfEyes = int(input("Enter the amount of eyes the alien has: "))

print("The aliens that could match your description are:")
if amountOfAntennae >= 3 and amountOfEyes <= 4:
    print("Dalek")
if amountOfAntennae <= 7 and amountOfEyes >= 2:
    print("Sontaran")
if amountOfAntennae < 0 and amountOfEyes < 0:
    print("Doesn't match any aliens")
elif amountOfAntennae <= 2 and amountOfEyes <= 3:
    print("Cyberman")
if amountOfAntennae > 8:
    print("Doesn't match any aliens")
