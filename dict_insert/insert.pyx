"""
Cython implementation of a dictionary insert
"""


cpdef dict test(int x):
    cdef dict d = {}
    cdef int i
    for i in range(x):
        d[i] = i

    return d
