#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1:
        val1a = tuple_a[0]
        val1b = tuple_a[1]
    elif len(tuple_a) == 1:
        val1a = tuple_a[0]
        val1b = 0
    else:
        val1a = 0
        val1b = 0
    if len(tuple_b) > 1:
        val2a = tuple_b[0]
        val2b = tuple_b[1]
    elif len(tuple_b) == 1:
        val2a = tuple_b[0]
        val2b = 0
    else:
        val2a = 0
        val2b = 0
    new_tuple = ((val1a + val2a), (val1b + val2b))
    return(new_tuple)
