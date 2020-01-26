from XYCoord import XYCoord

class WordSearchLetter(object):
    """
    The WordSearchLetter class is intended to hold a letter and the underlying coordinates of that letter.
    """
    def __init__(self, letter:str, coord:XYCoord):
        if not (isinstance(coord, XYCoord)):
            raise ValueError("coord must be an XYCoord instance")
        elif (coord.x < 0) or (coord.y < 0):
            raise ValueError("X/Y coordinates must be zero or positive integers")
        if (len(letter) > 1) or (len(letter) == 0):
            raise ValueError("Can only intialize WordSearchLetter with a single letter.")
        if (letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            raise ValueError("A WordSearchLetter must be a capital letter A-Z")
        self.coord = coord
        self.letter = letter

    def __str__(self):
        return self.letter

    def getCoordStr(self):
        return str(self.coord)