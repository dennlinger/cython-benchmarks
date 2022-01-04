"""
Central eval module
"""

import timeit

if __name__ == "__main__":

    x_try = """\
cross_product([1, 4], [3, 2])
    """
    x = timeit.timeit(x_try, setup="from tup_py_ref import cross_product", number=1000000)
    print(f"Python took {x:.4f} s to execute.")

    y_try = """\
cross_product([1,4], [2,3])
    """
    y = timeit.timeit(y_try, setup="from tup import cross_product; import numpy as np", number=1000000)
    print(f"Cython took {y:.4f} s to execute.")


    print(f"Cython has a speedup of {x/y:.2f} over Python.")
