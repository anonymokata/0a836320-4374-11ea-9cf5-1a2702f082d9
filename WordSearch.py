from enum import Enum, auto
from XYLines import CoordinateProducer, Direction, XYCoord, LineType
from copy import copy


class WordSearchLine(object):
    """
    The WordSearchLine object is an abstraction of a "line of text".  
    This particular line of text, however, originated from a WordSearch puzzle game.

    As such, this line of text shall be instantiated with a few pieces of information:
    1. The actual ASCII line of text stripped from the wordsearch game
    2. The "type" of line it is (possibilities are Forwardslash, Backslash, Row, or Column
    3. The coordinate of the starting letter of the line in the WordSearch
    """
    line = None              #the actual line, the entire line from the word search block
    linetype = None          #the type of line this is (row, col, forwardslash, backslash)
    length = None            #the length of the line
    startcoord = None        #the starting coordinate of the line
    endcoord = None          #the ending coordinate of the line
    searchdirection = None   #the search direction the word was found
    wordstartcoord = None    #the position of the word, if found
    coords = None            #coordinates of the discovered word(s)

    def __init__(self, line:list, linetype:LineType, startcoord:XYCoord):
        if (type(line) != list):
            raise ValueError("line argument must contain a list of WordSearchLetter objects")
        for x in line:
            if not isinstance(x, WordSearchLetter):
                raise ValueError("line argument must contain a list of WordSearchLetter objects")
        self.line = line
        self.length = len(line)
        self.linetype = linetype
        self.startcoord = startcoord  #the starting coordinate of the line
        self.endcoord = copy(CoordinateProducer(self.startcoord, self.linetype, Direction.Forward, 0, self.length-1).startcoord)   #use coordinate producer to get the coord at the opposite end
        self.coords = list()
        return

    def __contains__(self, teststring:str):
        """
        By using the __contains__ method, the 'in' operator becomes available to users.
        """
        if teststring in self.line:
            self.searchdirection = Direction.Forward
            startchar = self.line.find(teststring)
            self.__fillCoords(self.startcoord, startchar, len(teststring))    #we know the value is there, we know the direction it was found, and we know the start coordinate of the word
            return True
        elif teststring in self.line[::-1]:                  #reverse the contents of the line to figure out of the string is there in reverse
            self.searchdirection = Direction.Backward
            startchar = self.line[::-1].find(teststring)
            #use the end coordinates of the line as the starting point when searching in reverse
            self.__fillCoords(self.endcoord, startchar, len(teststring))    #we know the value is there, we know the direction it was found, and we know the start coordinate of the word
            return True
        else:
            self.searchdirection = None
            return False

    def search(self, teststring:str):
        """
        Wrapper around __contains__ so user is not FORCED to use in operator
        """
        return self.__contains__(teststring)

    def __fillCoords(self, startcoord:XYCoord, offset:int, length:int):
        """
        Get the coordinates of all characters in the searched word
        """
        cp = CoordinateProducer(startcoord, self.linetype, self.searchdirection, length, offset)
        self.coords = cp.getCoords()
        return


