#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """Class That defines a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize the width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes an instance of the Rectangle Class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to get area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that gets the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size."""
        return cls(size, size)

    def __str__(self):
        """Method to print a rectangle as a string of given characters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join([str(self.print_symbol) * self.__width
                         for i in range(self.__height)])
        return rec

    def __repr__(self):
        """function for string representation to create new instance"""
        wid = str(eval('self.width'))
        hgt = str(eval('self.height'))

        return "Rectangle(" + wid + ", " + hgt + ")"
