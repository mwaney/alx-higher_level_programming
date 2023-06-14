#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_uniq = set(my_list)
    res = 0
    for num in my_uniq:
        res += num
    return res
