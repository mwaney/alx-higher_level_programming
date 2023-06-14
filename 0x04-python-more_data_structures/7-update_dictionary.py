#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    keys_list = list(a_dictionary.keys())
    if key in keys_list:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
