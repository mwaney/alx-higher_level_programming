#!/usr/bin/python3
"""This function prints the
first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """prints introduction of a person.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
        Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        None: This function doesn't return a value
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    message = "My name is {} {}".format(first_name, last_name)
    print(message)
