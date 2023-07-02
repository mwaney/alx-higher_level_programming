#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class that tests to get the max integer
    """

    def test_module_docstring(self):
        """Tests for module docsting"""
        moDocStr = __import__('6-max_integer').__doc__
        self.assertTrue(len(moDocStr) > 1)

    def test_function_docstring(self):
        """Tests function docstring"""
        funcDocStr = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(funcDocStr) > 1)

    def test_max_integer(self):
        """
        Test the max integer in a list of integers
        """
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 7, 4]), 7)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([20, -20, 20]), 20)

    def test_empty(self):
        """Tests for no arguments passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negative(self):
        """Tests for list with all negative numbers"""
        list1 = [-6, -15, -54, -1, -100]
        self.assertEqual(max_integer(list1), -1)

    def test_other_types(self):
        """Tests for list with types that are not int"""
        list1 = [4, "World", True, 56, 3.2]
        with self.assertRaises(TypeError):
            max_integer(list1)


if __name__ == "__main__":
    unittest.main()
