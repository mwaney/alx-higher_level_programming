#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """True if obj is instance of class that
    it inherits from or is subclass of
    Otherwise it return False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
