"""
Evaluation of matrix multiplication function
"""

from cpython cimport array
import array

cpdef (int, int) cross_product(list x, list y):
    return x[0] * y[1], x[1] * y[0]
