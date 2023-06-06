#!/usr/bin/python3

def uppercase(str):
    word = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) < 123:
            word = word + chr(ord(letter) - 32)
        else:
            word += letter
    print("{}".format(word))
