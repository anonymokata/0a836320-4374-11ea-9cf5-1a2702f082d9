from XYCoord import XYCoord
from enum import Enum, auto
from copy import copy

"""
XYLines contains classes that have to do with x,y lines and the creation of coordinates representing those lines.
"""

class LineType(Enum):
    Row = auto()
    Column = auto()
    Forwardslash = auto()
    Backslash = auto()

class Direction(Enum):
    Forward = auto()
    Backward = auto()

class XDir(Enum):
    Left = -1
    Right = 1
    Still = 0

class YDir(Enum):
    Up = -1
    Down = 1
    Still = 0

class CoordinateProducer(object):
    """
    Given a starting coordinate, a direction, and a linetype, we will produce a list of coordinate objects
    That increment in the given direction with the given distance.
    Optionally provide an offset to start from a given position
    """
    linetype = None
    direction = None
    startcoord = None
    length = None
    coords = None
    offset = 0
    incrementx = XDir.Still.value
    incrementy = YDir.Still.value

    def __init__(self, startcoord:XYCoord, linetype:LineType, direction:Direction, length:int, offset:int=0):
        self.linetype = linetype
        self.direction = direction 
        self.startcoord = copy(startcoord)  #don't alter the startcoord coming in
        self.length = length
        self.offset = offset  #offset along this line in the given direction
        self.setIncrements()
        if (self.offset > 0):
            self.updateStartCoord(offset)

    def setLineType(self, linetype:LineType):
        self.linetype = linetype

    def setDirection(self, direction:Direction):
        self.direction = direction

    def setStartCoord(self, startcoord:XYCoord):
        self.startcoord = startcoord

    def setLength(self, length:int):
        self.length = length
    
    def getCoords(self):
        self.__fillCoords()
        return self.coords

    def setIncrements(self):
        if (self.linetype == LineType.Row):
            self.incrementy = YDir.Still.value
            if (self.direction == Direction.Forward): 
                self.incrementx = XDir.Right.value          # search is starting from left going right
            else:
                self.incrementx = XDir.Left.value           # search is starting from right going left
        elif (self.linetype == LineType.Column):
            self.incrementx = XDir.Still.value
            if (self.direction == Direction.Forward):
                self.incrementy = YDir.Down.value           # search is starting from top of col going down
            else:
                self.incrementy = YDir.Up.value             # search is starting from bottom of col going up
        elif (self.linetype == LineType.Forwardslash):
            if (self.direction == Direction.Forward):
                self.incrementx = XDir.Right.value          # search is starting from bottom of forward slash (/) going up and right
                self.incrementy = YDir.Up.value
            else:
                self.incrementx = XDir.Left.value           # search is starting from top of forward slash (/) going down and left
                self.incrementy = YDir.Down.value
        elif (self.linetype == LineType.Backslash):
            if (self.direction == Direction.Forward):  
                self.incrementx = XDir.Right.value          # search is starting from top of backslash (\) going down and right
                self.incrementy = YDir.Down.value
            else:
                self.incrementx = XDir.Left.value           # search is starting from bottom of backslash (\) going up and left
                self.incrementy = YDir.Up.value

    def updateStartCoord(self, offset):
        for i in range(self.offset):
            #update the startcoord in place
            self.startcoord.x += self.incrementx
            self.startcoord.y += self.incrementy

    def __fillCoords(self):
        """
        We simply generate a list of coordinates going in the specified direction
        """
        self.coords = list()
        self.coords.append(self.startcoord)  #first value is the starting coordinate
        for i in range(self.length-1):   #we already added one coord so no need for more
            #create a new coordinate with the previous value incremented accordng to the direction and type of search
            self.coords.append(XYCoord(self.coords[i].x + self.incrementx, self.coords[i].y + self.incrementy))
