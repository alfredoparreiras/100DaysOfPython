import random

word_list = ["alfredo", "carolina", "Marcely"]

# Remember to use random.choice - Should be a cleaner sintaxe here.
word = word_list[random.randint(0, len(word_list) - 1)]

empty_list = []
for char in range(len(word)):
    empty_list.append("_")

letter = input("Guess a letter.")

for i, char in enumerate(word):
    if char.lower() == letter.lower():
        empty_list[i] = letter.lower()

print(empty_list)


