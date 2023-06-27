#!/usr/bin/python3
"""Define a class called Magic Class"""
import math


class MagicClass:
    """
    Initialize Magic Class
    methods: area and circumference
    """
    def __init__(self, radius=0):
        """Initialization of Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Compute the Area"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Compute the circumference"""
        return 2 * math.pi * self.__radius
