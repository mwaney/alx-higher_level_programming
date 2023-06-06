#!/usr/bin/python3
for character in range(122, 96, -1):
    if character % 2 == 1:
        character -= 32
    print(chr(character), end = "")
