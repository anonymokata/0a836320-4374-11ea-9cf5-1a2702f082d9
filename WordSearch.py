from enum import Enum, auto


class LineType(Enum):
    Row = auto()
    Column = auto()
    Forwardslash = auto()
    Backslash = auto()

class SearchDir(Enum):
    Forward = auto()
    Backward = auto()

class XYCoord(object):
    """
    A simple abstraction of a tuple that we can get "x" and "y" from a coordinate
    instead of having to use array references, also gives use string representation
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

class WordSearchLine(object):
    """
    The WordSearchLine object is an abstraction of a "line of text".  This particular line of text, however, originated from a WordSearch puzzle game.
    As such, this line of text shall be instantiated with a few pieces of information:
    1. The actual ASCII line of text
    2. The "type" of line it is (possibilities are Forwardslash, Backslash, Row, or Column
    3. The coordinate of the starting letter of the line in the WordSearch
    """
    line = None
    linetype = None
    length = None
    startcoord = None
    searchdirection = None
    coords = None

    def __init__(self, line:str, linetype:LineType, startcoord:XYCoord):
        self.line = line
        self.length = len(line)
        self.linetype = linetype
        self.startcoord = startcoord  #the starting coordinate of the line
        self.coords = list()
        return

    def __contains__(self, teststring:str):
        """
        By using the __contains__ method, the 'in' operator becomes available to users
        """
        if teststring in self.line:
            self.searchdirection = SearchDir.Forward
            self.fillcoords(teststring)
            return True
        elif teststring in self.line[::-1]:    #reverse the contents of the line to figure out of the string is there in reverse
            self.searchdirection = SearchDir.Backward
            self.fillcoords(teststring)
            return True
        else:
            self.searchdirection = None
            return False

    def fillrowcoords(self, teststring:str):
        """
        this will fill the 'coords' list with a list of XYCoords representing the coordinates of each letter
        if the string is a 'row' we need to keep row number (y) constant and update col (x) for each coordinate
        """
        if self.searchdirection == SearchDir.Forward:
            """
            if input is ABCHELLOXYZ, startx is 3 when looking for "HELLO"
            coords should be (3,y) (4,y) ... (7,y)
            """
            startx = self.line.find(teststring)   #the position that the string is found
            for x in range(startx,(startx+len(teststring)),1):
                coord = XYCoord(self.startcoord.x, self.startcoord.y)
                coord.x = x                       #update only x coordinate
                self.coords.append(coord)

        elif self.searchdirection == SearchDir.Backward:
            """
            if input is ABCHELLOXYZ, startx should be 7 when looking for "OLLEH"
            coords should be (7,y) (6,y) ... (3,y)
            """
            startx = self.line.find(teststring[::-1])   #the position that the string is found when reversed into ZYXOLLEHCBA
            startx = self.length - startx - 1           #if found at position 3 in reversed string, 'true' position is 7, so line length - startx - 1 (to account for zero start pos)
            for x in range(startx,(startx-len(teststring)),-1):    #counting backwards
                coord = XYCoord(self.startcoord.x, self.startcoord.y)
                coord.x = x                             #update only x coordinate
                self.coords.append(coord)

    def fillcoords(self, teststring:str):
        if self.linetype == LineType.Row:
            self.fillrowcoords(teststring)