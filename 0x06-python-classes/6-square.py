#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """A squre class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Gets instance of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        area is a public instance method

        Returns:
            int: the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        print("\n".join([" " * self.position[0] +
                        "#" * self.size
                         for i in range(self.size)]))
