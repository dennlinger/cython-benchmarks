"""
Central eval module
"""

import timeit

if __name__ == "__main__":

    x = timeit.timeit("insert_py_ref.test(10)", setup="import insert_py_ref", number=100000)
    print(f"Python took {x:.4f} s to execute.")

    y = timeit.timeit("insert.test(10)", setup="import insert", number=100000)
    print(f"Cython took {y:.4f} s to execute.")

    print(f"Cython has a speedup of {x/y:.2f} over Python.")
