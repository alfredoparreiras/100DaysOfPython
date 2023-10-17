import string
import random

LETTERS = list(string.ascii_lowercase)
SYMBOLS = list(string.punctuation)
NUMBERS = list(range(10))


print("### Welcome to the PyPassword Generator!")
letters_quantity = int(input("How many letters would you like in your password?"))
symbols_quantity = int(input("How many symbols would you like in your password?"))
numbers_quantity = int(input("How many numbers would you like in your password?"))

# Retrieving Random Numbers to build password.
password_list = []
password_string = ''
for char in range(1, letters_quantity + 1):
    password_list.append(random.choice(LETTERS))


for char in range(1, symbols_quantity + 1):
    password_list.append(random.choice(SYMBOLS))

for char in range(1, numbers_quantity + 1):
    password_list.append(str(random.choice(NUMBERS)))

random.shuffle(password_list)
password_string = "".join(password_list)
print(f"Your suggested password is {password_string}, containing {len(password_string)} characters.")