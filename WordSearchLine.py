from enum import Enum, auto
from XYLines import CoordinateProducer, Direction, XYCoord, LineType
from WordSearchLetter import WordSearchLetter
from copy import copy

class WordSearchMatch(object):
    """
    A simple abstraction of a "match"
    """
    def __init__(self, startpos:int, length:int, direction:Direction):
        self.startpos = startpos
        self.length = length
        self.direction = direction

class WordSearchLine(object):
    """
    The WordSearchLine object is an abstraction of a "line of text".  
    This particular line of text, however, originated from a WordSearch puzzle game.
    The line will be instantiated with a list of WordSearchLetter objects.
    """
    line = None              #the actual line, the entire line from the word search block
    matches = None           #list of discovered matches

    def __init__(self, line:list):
        if (type(line) != list):
            raise ValueError("line argument must contain a list of WordSearchLetter objects")
        for x in line:
            if not isinstance(x, WordSearchLetter):
                raise ValueError("line argument must contain a list of WordSearchLetter objects")
        self.line = line
        return

    def toString(self):
        """
        return a string representation of the WordSearchLetter objects in this list
        """
        return ''.join([x.letter for x in self.line])

    def search(self, teststring:str):
        """
        a wrapper around __contains__ if users don't like the 'in' notation.
        WordSearchLine.search('foo') will return TRUE if 'foo' was found in the line.
        Alternatively, can use 'foo' in wsl, where wsl is a WordSeachLine object.
        """
        return self.__contains__(teststring)

    def __contains__(self, teststring:str):
        """
        By using the __contains__ method, the 'in' operator becomes available to users.
        """
        me = self.toString()
        me_backwards = me[::-1]    #reverse the string
        teststringlen = len(teststring)
        self.matches = list()      #clear existing list of matches
        found = False

        #test the local var for the match both forwards and backwards, and push those answers into the matches list
        if teststring in me:
            startpos = me.find(teststring)
            self.matches.append(WordSearchMatch(startpos, teststringlen, Direction.Forward))
            found = True
        if teststring in me_backwards:
            startpos = me_backwards.find(teststring)
            self.matches.append(WordSearchMatch(startpos, teststringlen, Direction.Backward))
            found = True

        if not found:
            self.searchdirection = None

        return found