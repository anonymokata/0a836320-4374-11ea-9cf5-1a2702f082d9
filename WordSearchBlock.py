from XYCoord import XYCoord
from WordSearchLetter import WordSearchLetter
from WordSearchLine import WordSearchLine

class WordSearchBlock(object):
    """
    A WordSearchBlock has the following responsibilities:
    1. Holding the block letters that represent the Word Search game
    1a. Validating that the block is sized appropriately
    2. The letters are each represented by WordSearchLetter objects, each is tagged with its position (coordinates) in the grid
    3. The WordSearchBlock object will also be responsible for 'slicing' the block into rows, columns, and diagonal WordSearchLines
    
    Note: The WordSearchBlock is NOT responsible for solving the puzzle.
    """
    width = None
    height = None
    block = None

    def __init__(self, letters:list):
        """
        Init the WordSearchBlock with a two-dimensional array of lists.  The list returned by letters[0] is the top line of the puzzle.
        """
        self.block = list()

        y = 0
        for row in letters:
            if len(row) != len(letters[0]):
                raise ValueError("The length of each row of letters must be the same.")

            x = 0
            newrow = list()
            for let in row:
                newrow.append(WordSearchLetter(let, XYCoord(x,y)))
                x += 1

            self.block.append(newrow)
            y += 1
        
        self.width = len(letters[0])
        self.height = len(letters)

    def getRow(self, rownum:int):
        """
        return a single row from the block
        """
        return WordSearchLine(list(self.block[rownum]))

    def getCol(self, colnum:int):
        """
        return a single column from the block
        """
        return WordSearchLine([x[colnum] for x in self.block])

    def getFwdSlashStartPos(self, slashnum:int):
        """
        See getFwdSlash for description of slashes.  This function will determine the start position
        for a forward slash given the slash number.
        """
        if slashnum > (self.height-1):
            startx = slashnum-(self.height-1)
            starty = (self.height-1)
        if slashnum <= (self.height-1):
            startx = 0
            starty = slashnum
        
        return XYCoord(startx, starty)

    def getBackSlashStartPos(self, slashnum:int):
        """
        See getBackSlash for description of slashes.  This function will determine the start position
        for a back slash given the slash number.
        """
        if slashnum > (self.height-1):
            startx = ((self.height-1)-slashnum)+(self.width-1)  #for every number larger than height, we go backwards from width
            starty = (self.height-1)
        if slashnum <= (self.height-1):
            startx = (self.width-1)
            starty = slashnum
        
        return XYCoord(startx, starty)

    def getFwdSlash(self, slashnum:int):
        """
        Starts at the top left corner of the block and attempts to get "forward slash" slices, (/),
        that is, diagnoal slices going from southwest --> northeast
        for a 6x6 block, slashnum is as follows:

          0 1 2 3 4 5
          1 2 3 4 5 6
          2 3 4 5 6 7
          3 4 5 6 7 8
          4 5 6 7 8 9
          5 6 7 8 9 A

        when user wants fwd slash '3', they will get coordinates: 0,3 1,2 2,1 3,0
        when user wants fwd slash '8', they will get coordinates: 3,5 4,4 5,4

        properties of fwdslash when looping:
        * xpos is always increasng from startposx
        * ypos is always decreasing from startposy
        """
        slashlist = list()

        xincrement = 1
        yincrement = -1

        pos = self.getFwdSlashStartPos(slashnum)

        #as long as pos stays within the block, continue to iterate
        while (pos.x >= 0) and (pos.x <= self.width-1) and (pos.y >=0) and (pos.y <= self.height-1):
            slashlist.append(self.block[pos.y][pos.x])
            pos.x += xincrement
            pos.y += yincrement

        return WordSearchLine(slashlist)

    def getBackSlash(self, slashnum:int):
        """
        Starts at the top right corner of the block and attempts to get "back slash" slices, (\\),
        that is, diagnoal slices going from southeast --> northwest
        for a 6x6 block, slashnum is as follows:

          5 4 3 2 1 0
          6 5 4 3 2 1
          7 6 5 4 3 2
          8 7 6 5 4 3
          9 8 7 6 5 4
          A 9 8 7 6 5

        when user wants back slash '3', they will get coordinates: 5,3 4,2 3,1 2,0
        when user wants back slash '8', they will get coordinates: 2,5 1,4 0,3

        properties of fwdslash when looping:
        * xpos is always decreasing from startposx
        * ypos is always decreasing from startposy
        """
        slashlist = list()

        xincrement = -1
        yincrement = -1

        pos = self.getBackSlashStartPos(slashnum)

        #as long as pos stays within the block, continue to iterate
        while (pos.x >= 0) and (pos.x <= self.width-1) and (pos.y >=0) and (pos.y <= self.height-1):
            slashlist.append(self.block[pos.y][pos.x])
            pos.x += xincrement
            pos.y += yincrement

        return WordSearchLine(slashlist)

    def getAllSlices(self):
        """
        A helper function to get all types of slices to be used for searching.  Will get rows, columns, and slashes.
        """
        allslices = list()
        allslices.extend([self.getRow(i) for i in range(self.height)])
        allslices.extend([self.getCol(i) for i in range(self.width)])
        allslices.extend([self.getFwdSlash(i) for i in range(self.width + self.height - 1)])
        allslices.extend([self.getBackSlash(i) for i in range(self.width + self.height - 1)])
        
        return allslices