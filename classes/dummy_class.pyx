"""
Experimentation with different class levels
"""

cdef class Dummy:
    cdef int x, y
    def __init__(self,int x,int y):
        self.x = x
        self.y = y

    cdef int _square(self):
        return self.x * self.y

    def square(self):
        return self._square()


cdef class CpDummy:
    cdef int x, y
    def __init__(self,int x,int y):
        self.x = x
        self.y = y

    cpdef int square(self):
        return self.x * self.y


class Abstract:
    def __init__(self, int z):
        self.z = z

class PyDummy(Dummy, Abstract):
    def __init__(self, x, y, z):
        Dummy.__init__(self, x, y)
        Abstract.__init__(self, z)

    def volume(self):
        return self.square() * self.z