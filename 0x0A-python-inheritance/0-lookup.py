#!/usr/bin/python3
"""
Contains the lookup fucntion that returns
list of object's attribute and methods
"""


def lookup(obj):
    """returns a list of an object's attribute and methods"""
    return dir(obj)
