#!/usr/bin/python3
"""
Module from a function that multiplies 2 matrices
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices
    m_a first matrix
    m_b second matrix

    returns: result of the mutiplication
    """

    return (np.matmul(m_a, m_b))
