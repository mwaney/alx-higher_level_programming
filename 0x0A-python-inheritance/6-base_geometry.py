#!/usr/bin/python3
"""
Contains class BaseGeometry
with public instance method area
"""


class BaseGeometry:
    """
    A class with a method area
    """
    def area(self):
        """
        raises an exception when callsed
        because it is not implemented
        """
        raise Exception("area() is not implemented")
