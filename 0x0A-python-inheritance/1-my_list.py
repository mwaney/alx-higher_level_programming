#!/usr/bin/python3
"""
contains the MyList class that inherits from list
"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list in ascending order"""
        print(sorted(self))
