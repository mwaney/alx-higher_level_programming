#!/usr/bin/python3
"""
This is a script defining a Square class as a subclass of Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
     Square class representing a square shape.
    Inherits from the Rectangle class.
    """
    def __init__(self, size):
        """
        Initialize a Square object with a given size.
        Validates that the size is an integer using the
        integer_validator method.
        Calls the constructor of the parent class
        (Rectangle) with the size parameter twice
        to create a square with equal width and height.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
         Return a string representation of the Square object.
        Format: "[Square] size/size"
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
