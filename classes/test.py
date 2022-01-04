"""
Central eval module
"""

import timeit
from dummy_class import PyDummy

if __name__ == "__main__":

    x_try = """\
a = Dummy(3, 4);
a.square()
    """
    x = timeit.timeit(x_try, setup="from dummy_class_py_ref import Dummy", number=10000)
    print(f"Python took {x:.4f} s to execute.")

    y_try = """\
a = Dummy(3, 4);
a.square()
    """
    y = timeit.timeit(y_try, setup="from dummy_class import Dummy", number=10000)
    print(f"Cython took {y:.4f} s to execute.")

    print(f"Cython has a speedup of {x/y:.2f} over Python.")

    pd = PyDummy(2, 3, 5)
    pd.volume()