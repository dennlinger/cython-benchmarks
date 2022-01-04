

class Dummy:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y