#!/usr/bin/python3
"""numpy module"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
     Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    """

#   a = np.array(m_a)
#    b = np.array(m_b)
    result = np.matmul(m_a, m_b)

    return result
