import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



print("### Welcome to Rock - Paper - Scissors AI game")
user_name = input("Enter your name: ")
user_move = input("Please Select (R)ock, (P)aper, (S)cissors as your move. Choose R, P or S => ").upper()

computer_move_generator = random.randint(1,3);
computer_move = None

if computer_move_generator == 1:
    computer_move = "R"
elif computer_move_generator == 2:
    computer_move = "P"
elif computer_move_generator == 3:
    computer_move = "S"
else:
    print("There is a problem with Computer Generator Algorith.")

# Setting Victory
if user_move == "R":
    if computer_move == "R":
        print(f"{user_name} chose ROOOCK \n {ROCK} \n\n And Computer chose ROOOCK \n {ROCK} \nIt's a TIE! ")
    elif computer_move == "S":
        print(f"{user_name} chose ROOOCK \n {ROCK} \n\n And Computer chose SCISSORSS \n {SCISSORS} \n{user_name} WINS! ")
    else:
        print(f"{user_name} chose ROOOCK \n {ROCK} \n\n And Computer chose PAPER \n {PAPER} \nComputer its the Bigger Winner! ")
elif user_name == "P":
    if computer_move == "R":
        print(f"{user_name} chose PAAAAPER \n {PAPER} \n\n And Computer chose ROOOCK \n {ROCK} \n{user_name} WINS ")
    elif computer_move == "P":
        print(f"{user_name} chose PAAAAPER \n {PAPER} \n\n And Computer chose PAAAAAPER \n {PAPER} \n{user_name} Its a TIE!!! ")
    else:
        print(f"{user_name} chose PAAAAPER \n {PAPER} \n\n And Computer chose SCISSORS \n {SCISSORS} \nComputer its the Bigger Winner! ")
else:
    if computer_move == "P":
        print(f"{user_name} chose SCISSORRRS \n {SCISSORS} \n\n And Computer chose PAAAAPER \n {PAPER} \n{user_name} WINS ")
    elif computer_move == "S":
        print(f"{user_name} chose SCISSORRRS \n {SCISSORS} \n\n And Computer chose SCISSORS \n {SCISSORS} \n{user_name} Its a TIE!!! ")
    else:
        print(f"{user_name} chose SCISSORRRS \n {SCISSORS} \n\n And Computer chose SCISSORS \n {ROCK} \nComputer its the Bigger Winner! ")