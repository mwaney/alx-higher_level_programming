#!/usr/bin/python3
"""
This is a module to add two numbers
The numbers to be added can be integers
or floats
"""


def add_integer(a, b=98):
    """Adds two integers or floats and returns the sum as an integer.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added.
        Defaults to 98.

    Raises:
        TypeError: If a is not an integer or float.
        TypeError: If b is not an integer or float.

    Returns:
        int: The sum of a and b, converted to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
