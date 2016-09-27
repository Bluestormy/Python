# Copyright (c) 2016 Kyle George. You may share and distribute my code as long as this notice stays in place. Enjoy!
"""
This Python Encrypter works on the principle of the Caesar Cipher and the Substitution Cipher, Might use basic equation (y = (x+k) % 26)
For this, set the position of A to 0 and set Z to 26. See Below For an example of the alphabet with index numbers
A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
"""
from time import sleep # importing the sleep function to simulate the program thinking
print("PyCrypter, your personal python encrypter has started")#Startup message
sleep(1)
print("Loading Resources...")
sleep(2)
code = ""
alphabet = {0: " ", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
            12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V",
            23: "W", 24: "X", 25: "Y", 26: "Z", 27: "_"}


def select_mode():# Allows the user to select the mode; either Encrypt or Decrypt
    choice = raw_input("Would you like to Encrypt or Decrypt the message?: ")
    frmt_choice = choice.lower()# formatting the choice to lowercase
    if frmt_choice == "encrypt":
        sleep(1)
        encrypt()# run the encrypt function if the user chooses "encrypt"
        exit()
    if frmt_choice == "decrypt":
        sleep(1)
        decrypt()# run the decrypt function if the user chooses "decrypt"
        exit()
    elif frmt_choice != "decrypt" or frmt_choice != "encrypt":
        sleep(1)
        print("Oh No! You've Entered Gibberish! I was not made for Gibberish!")
        sleep(1)
        exit()

keys = alphabet.keys()# store the keys of the alphabet dictionary in the variable "keys"
values = alphabet.values()# store the values of the alphabet dictionary in the variable "values"


def encrypt():# Encrypt function
    key_shift = int(raw_input("Please input the Key Shift(Numbers Only!): "))# collect key shift
    raw_msg = raw_input("Please input the message which you wish to encrypt: ")# collect message
    msg = raw_msg.upper()# change message to uppercase
    encrypted_msg = []
    letter_encrypted = []
    for i in msg:
        num_val = keys[values.index(i)] + key_shift
        if num_val > 26:
            num_val -= 26
            if num_val == key_shift:# ensure that the letter number does not coincide with the number assigned to space
                num_val = 27 
        encrypted_msg.append(num_val)
    result = [alphabet[i] for i in encrypted_msg]
    letter_encrypted.append(result)
    for i in result:
        count = 1
        while count == 1:
            result_str = str(result)
            result_str = result_str.translate(None, " [],''")
            print(result_str.replace("", ""))
            count += 1
            exit()


def decrypt():
    key_shift = int(raw_input("Please input the Key Shift(Numbers Only!): "))
    raw_msg = raw_input("Please input the message which you wish to encrypt: ")
    msg = raw_msg.upper()
    decrypted_msg = []
    for i in msg:
        num_val = keys[values.index(i)] - key_shift
        if num_val < 0:
            num_val += 26
            if num_val == 0:
                num_val = 27
        decrypted_msg.append(num_val)
    result = [alphabet[i] for i in decrypted_msg]
    print(result)
    for i in result:
        count = 1
        while count == 1:# This is in a while loop, like so to ensure that the answr is only printed once
            result_str = str(result)
            result_str = result_str.translate(None, "[],''")# remove any [](square brackets, commas and quotes when printed
            print(result_str.replace("", ""))
            count += 1
            exit()

select_mode()
