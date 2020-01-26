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
    4. The WordSearchBlock is NOT responsible for solving the puzzle.
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
                raise ValueError("The length of each row of letters must be the same")
            if len(row) != len(letters):
                raise ValueError("The length of each row of letters must match the height of the block")

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
        return WordSearchLine(list(self.block[rownum]))

    def getCol(self, colnum:int):
        return WordSearchLine([x[colnum] for x in self.block])

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

        slashnum 0 = len 1  startpos(0,0)
                 1 = len 2  startpos(0,1)
                 2 = len 3  startpos(0,2)
                 3 = len 4  startpos(0,3)
                 4 = len 5  startpos(0,4)
                 5 = len 6  startpos(0,5)  <--- height-1
                 6 = len 5  startpos(1,5)
                 7 = len 4  startpos(2,5)
                 8 = len 3  startpos(3,5)
                 9 = len 2  startpos(4,5)
                 A = len 1  startpos(5,5)

        when user wants fwd slash '3', they will get coordinates: 0,3 1,2 2,1 3,0
        when user wants fwd slash '8', they will get coordinates: 3,5 4,4 5,4

        properties of fwdslash when looping:
        * xpos is always increasng from startposx
        * ypos is always decreasing from startposy

        * when slashnum > height-1, startposy = height-1
        * when slashnum <= height-1, startposx = 0
        * length of slice is (startposy+1 - startposx)

        """
        slashlist = list()

        xincrement = 1
        yincrement = -1


        if (slashnum <= self.height-1):
            startposx = 0
            startposy = slashnum
        if (slashnum > self.height-1):
            startposx = slashnum-(self.height-1)
            startposy = self.height-1

        posx = startposx
        posy = startposy

        for inc in range(startposy+1 - startposx):
            slashlist.append(self.block[posy][posx])
            posx += xincrement
            posy += yincrement

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

        slashnum 0 = len 1  startpos(5,0)
                 1 = len 2  startpos(5,1)
                 2 = len 3  startpos(5,2)
                 3 = len 4  startpos(5,3)
                 4 = len 5  startpos(5,4)
                 5 = len 6  startpos(5,5)  <--- height-1
                 6 = len 5  startpos(4,5)
                 7 = len 4  startpos(3,5)
                 8 = len 3  startpos(2,5)
                 9 = len 2  startpos(1,5)
                 A = len 1  startpos(0,5)

        when user wants back slash '3', they will get coordinates: 5,3 4,2 3,1 2,0
        when user wants back slash '8', they will get coordinates: 2,5 1,4 0,3

        properties of fwdslash when looping:
        * xpos is always decreasing from startposx
        * ypos is always decreasing from startposy

        * when slashnum < height-1, startposx = height-1, length = startposy+1
        * when slashnum >= height, startposy = height-1, length = startposx+1
        """
        slashlist = list()

        xincrement = -1
        yincrement = -1

        if (slashnum <= self.height-1):
            startposx = self.height-1
            startposy = slashnum
            length = startposy+1
        if (slashnum > self.height-1):
            startposx = ((self.height-1)*2)-slashnum
            startposy = self.height-1
            length = startposx+1

        posx = startposx
        posy = startposy

        for inc in range(length):
            slashlist.append(self.block[posy][posx])
            posx += xincrement
            posy += yincrement

        return WordSearchLine(slashlist)