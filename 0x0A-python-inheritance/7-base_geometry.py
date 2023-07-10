#!/usr/bin/python3
"""
Contains class BaseGeometry
with public instance method area
"""


class BaseGeometry:
    """
    A class with a public method area and integer_validator
    """
    def area(self):
        """
        raises an exception when callsed
        because it is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ensures that type of value is int and greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
