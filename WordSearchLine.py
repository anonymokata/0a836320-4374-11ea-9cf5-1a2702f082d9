from enum import Enum, auto
from WordSearchLetter import WordSearchLetter
from copy import copy

class Direction(Enum):
    Forward = auto()
    Backward = auto()

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
    line = None              #the actual line, the entire line from the word search block, as WordSearchLetter instances
    matches = None           #list of discovered matches

    def __init__(self, line:list):
        if (type(line) != list):
            raise ValueError("line argument must contain a list of WordSearchLetter objects")
        for x in line:
            if not isinstance(x, WordSearchLetter):
                raise ValueError("line argument must contain a list of WordSearchLetter objects")
        self.line = line
        return

    def __len__(self):
        """
        allows use of len() on this list
        """
        return len(self.line)

    def __getitem__(self, index:int):
        """
        allows user to use [] when referring to this list
        """
        return self.line[index]

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
        This will allow the use of the 'in' operator on this list as if it were a string
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

    def get_result_as_string(self, index):
        """
        Helper method -- get the match from the list as a string.  The string will be formatted per the output requirement.
        """
        if (index + 1) > len(self.matches):
            raise ValueError("index is outside of matches array")

        m = self.matches[index]

        #special handling when match was found in reverse
        if m.direction == Direction.Backward:
            local_string = self.toString()[::-1]
            local_line = self.line[::-1]     #reverse the entire line locally
        else:
            local_string = self.toString()
            local_line = self.line           

        #use the local_string and local_line for results output
        found_string = local_string[m.startpos:(m.startpos+m.length)]                                #get the substring representing the match
        found_coords = ','.join( [str(x.coord) for x in local_line[m.startpos:(m.startpos+m.length)]] )  #the coordinates separated by commas

        return "{0}: {1}".format(found_string, found_coords)