#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as exp:
        stderr.write("Exception: {}\n".foramat(exp))
        return None
