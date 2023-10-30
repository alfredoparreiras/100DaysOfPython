import random

# The goal of the game is try to be closest as possible from 21
# if you get more than 21 when sum your cards, you "BUST" , it means
# You lose immediately.
# Cards from 2 to 10, counts as the face value.
# Cards J , Q and K counts as 10.
# A counts as 1 or 11.
# If dealer finsih with a hand smaller than 17, they must get a new card
#

# Create a List to represent the card deck.
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# GAME

print("""
                                                                                       
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
""")

user_cards = []
computer_cards = []


def calculate_score(cards):
    return sum(cards)


def check_winner(user, computer, user_deck, computer_deck):
    result = ""

    if (user > 21) or (user < computer < 21):
        result = (f"Your final hand : {user_deck} , final score: {user}\nComputer's final"
                  f" hand : {computer_deck}, final score: {computer}\n"
                  f"Computer won!")
    if (computer > 21) or (computer < user < 21):
        result = (f"Your final hand : {user_deck} , final score: {user}\nComputer's final"
                  f" hand : {computer_deck}, final score: {computer}\n"
                  f"User won!")

    if computer == user:
        result = (f"Your final hand : {user_deck} , final score: {user}\nComputer's final"
                  f" hand : {computer_deck}, final score: {computer}\n"
                  f"It's a draw!!")

    return result


def check_computer_move(computer):
    if computer < 17:
        return True
    return False


want_play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while want_play == 'y':
    is_result_ready = False
    user_cards = random.sample(CARDS, 2)
    computer_cards = random.sample(CARDS, 2)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards : {user_cards}, current score {user_score}")
    print(f"Computer's first card {computer_cards[0]}")
    action = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()

    while action == "y":
        user_cards += random.sample(CARDS, 1)
        user_score = calculate_score(user_cards)

        print(f"Your cards {user_cards}, current score {user_score}")
        print(f"Computer's first card {computer_cards[0]}")

        if (user_score > 21) or (computer_score > 21):
            action = 'n'
            print(check_winner(user_score, computer_score, user_cards, computer_cards))
        else:
            action = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()

    if not is_result_ready:
        print(check_winner(user_score, computer_score, user_cards, computer_cards))
    want_play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
