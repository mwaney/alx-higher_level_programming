#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Instantiating the class"""
    def __init__(self, size=0):
        """
        initializing a squre instance.

        Args:
            size (int): The size of the squuare(0 by default)
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        area is a public instance method

        Returns:
            int: the area of a square
        """
        return self.__size * self.__size 
