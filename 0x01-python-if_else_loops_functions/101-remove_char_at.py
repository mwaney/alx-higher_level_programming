#!/usr/bin/python3
def remove_char_at(str, n):
    if n > 0 and n <= len(str):
        new_string = str[:n] + str[n + 1:]
    else:
        new_string = str
    return new_string
