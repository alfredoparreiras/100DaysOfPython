import random

word_list = ["alfredo", "carolina", "Marcely"]
print("Welcome to Hangman.\nYou have to discover what word it is:")
word = random.choice(word_list).lower()

displa_list = ['_'] * len(word)
life = 4

while life > 0 and '_' in displa_list:
    letter = input(f"You have {life} lives. Make a guess and discover a letter: ").lower()

    if letter not in word:
        life -= 1
    else:
        for i, char in enumerate(word):
            if char == letter:
                displa_list[i] = letter

    print(''.join(displa_list))

if "_" not in displa_list:
    print("Congratulations! You won!")
else:
    print("Sorry, you lost. The word was", word)