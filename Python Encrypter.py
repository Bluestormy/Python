# Copyright (c) 2016 Kyle George. You may share and distribute my code as long as this notice stays in place. Enjoy!
"""
This Python Encrypter works on the basic equation (y = (x+k) % 26).
For this, set the position of A to 0 and set Z to 26. See Below For an example of the alphabet with index numbers
A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
"""
from time import sleep
print("PyCrypter, your personal python encrypter has started")
sleep(1)
print("Loading Resources...")
sleep(2)
code = ""
alphabet = {0: " ", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
            12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V",
            23: "W", 24: "X", 25: "Y", 26: "Z", 27: "_"}


def select_mode():
    choice = raw_input("Would you like to Encrypt or Decrypt the message?: ")
    frmt_choice = choice.lower()
    if frmt_choice == "encrypt":
        sleep(1)
        encrypt()
        exit()
    if frmt_choice == "decrypt":
        sleep(1)
        decrypt()
        exit()
    elif frmt_choice != "decrypt" or frmt_choice != "encrypt":
        sleep(1)
        print("Oh No! You've Entered Gibberish! I was not made for Gibberish!")
        sleep(1)
        exit()

keys = alphabet.keys()
values = alphabet.values()


def encrypt():
    key_shift = int(raw_input("Please input the Key Shift(Numbers Only!): "))
    raw_msg = raw_input("Please input the message which you wish to encrypt: ")
    msg = raw_msg.upper()
    encrypted_msg = []
    letter_encrypted = []
    for i in msg:
        num_val = keys[values.index(i)] + key_shift
        if num_val > 26:
            num_val -= 26
            if num_val == 10:
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
        while count == 1:
            result_str = str(result)
            result_str = result_str.translate(None, "[],''")
            print(result_str.replace("", ""))
            count += 1
            exit()

select_mode()