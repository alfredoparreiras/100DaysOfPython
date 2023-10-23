## Ceaser Cipher Project - 100 Days of Python Bootcamp
import string

# List with all letters
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#


def encrypt(plain_text, shift_amount):
    encryptedMessage = ""

    for letter in plain_text:
        if letter != " ":
            position = ALPHABET.index(letter)
            new_position = position + shift_amount
            new_letter = ALPHABET[new_position]
            encryptedMessage += new_letter
        else:
            encryptedMessage += letter

    return encryptedMessage


def decrypt(encrypted_message, shift_amount):
    plain_message = " "
    for letter in encrypted_message:
        if letter != " ":
            position = ALPHABET.index(letter)
            new_position = position - shift_amount
            new_letter = ALPHABET[new_position]
            plain_message += new_letter
        else:
            plain_message += letter

    return plain_message


method = ""
message = ""

while method != '0':
    print("Welcome to Ceaser Cipher")
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt and 0 to exit :").lower()
    if method == '0':
        break

    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number:"))

    if method == "encode":
        print(f"Your encrypted message is : {encrypt(message, shift_number)}")
    elif method == "decode":
        print(f"Your decrypted message is : {decrypt(message, shift_number)}")
    else:
        print("ERROR : You must type, 'encrypt' or 'decrypt'.")
