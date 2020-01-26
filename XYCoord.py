class XYCoord(object):
    """
    A simple abstraction of an X,Y point.
    """
    def __init__(self, x, y):
        if ((type(x) != int) or (type(y) != int)):
            raise ValueError("x and y coordinates must be integers")
        else:
            self.x = x
            self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)