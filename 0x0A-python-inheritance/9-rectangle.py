#!/usr/bin/python3
"""
Contains class BaseGeometry
with public instance method area
and a Rectangle subclass
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


class Rectangle(BaseGeometry):
    """A blueprint of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """extends parent method and returns
        the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representing the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
