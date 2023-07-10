#!/usr/bin/python3
""""
Function that adds new attribute to Objects
"""


def add_attribute(obj, attrib, val):
    """
    add a new attribute to object if possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attrib, val)
    else:
        raise TypeError("can't add new attribute")
