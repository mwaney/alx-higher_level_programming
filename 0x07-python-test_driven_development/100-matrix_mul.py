#!/usr/bin/python3
"""A matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(entry, list) for entry in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(entry, list) for entry in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(entry) == len(m_a[0]) for entry in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(entry) == len(m_b[0]) for entry in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_list = []
    for i in range(len(m_b[0])):
        new_entry = []
        for j in range(len(m_b)):
            new_entry.append(m_b[j][i])
        new_list.append(new_entry)

    new_matrix = []
    for row in m_a:
        new_entry = []
        for col in new_list:
            res = 0
            for i in range(len(new_list[0])):
                res += row[i] * col[i]
            new_entry.append(res)
        new_matrix.append(new_entry)

    return new_matrix
