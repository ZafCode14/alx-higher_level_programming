#!/usr/bin/python3
"""Module with a function"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices
    Args:
        m_a (list of lists of int / float): first matrix
        m_b (list of lists of int / float): second matrix
    Return:
        the result of the multiplication
    """
    return (numpy.matmul(m_a, m_b))
