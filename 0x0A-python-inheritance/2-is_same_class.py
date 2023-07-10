#!/usr/bin/python3
"""
This module contains the function is_same_class and
returns True for object which is exactly an instance of class
"""


def is_same_class(obj, a_class):
    """return true if obj is object is exactly
    an instance of the specified class"""
    return (type(obj) == a_class)
