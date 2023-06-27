#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """A squre class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """"private instance to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """private instance to set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area is a public instance method

        Returns:
            int: the area of a square
        """
        return self.__size * self.__size
