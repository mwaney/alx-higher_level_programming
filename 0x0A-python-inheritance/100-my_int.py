#!/usr/bin/python3
"""
Contain the class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt class representing a custom integer type.
    Inherits from the built-in int class.
    """
    def __new__(cls, *args, **kwargs):
        """
        Customizes the creation of a new instance of the class.
        Overrides the __new__ method to customize object creation.
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        Overrides the equality comparison operator
        (==) for MyInt objects. Returns the negation
        of the built-in equality comparison between self and other.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Overrides the inequality comparison operator (!=)
        for MyInt objects. Returns the result of the built-in
        equality comparison between self and other.
        """
        return int(self) == other
