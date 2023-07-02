#!/usr/bin/python3
"""Module for matrix multiplication using NumPy."""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Returns the product of 2 matrices"""
    return numpy.matmul(m_a, m_b)
