#!/usr/bin/python3


def no_c(my_string):
    new_str = ""
    to_rmv = 'c'
    to_rmv_2 = 'C'
    for ch in my_string:
        if ch != to_rmv and ch != to_rmv_2:
            new_str += ch
    return new_str
