# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
import random

names = input("Let's define who is pay the dinner. Enter the possible names "
              "\nPlease, use comma to separate the names: ")
namesList = names.split(",")
list_length = len(namesList)

if namesList[0] == "":
    print("You must enter any name")
else:
    chooser = random.randint(0, list_length - 1)
    print(f"{namesList[chooser]} is going to buy the meal today!")