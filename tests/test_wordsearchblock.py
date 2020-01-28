import pytest
from WordSearchLetter import WordSearchLetter
from WordSearchLine import WordSearchLine
from WordSearchBlock import WordSearchBlock
from XYCoord import XYCoord

class Test_WordSearchBlock:
    """
    Set up a block that we will used for testing in this test class
    """
    def setup_class(self):
        self.rawblock = list()
        #Words in here are:  FOOD, ADD, BEEF, LEER
        self.rawblock.append("F,O,O,D,X,Y".split(","))
        self.rawblock.append("A,X,Q,Z,U,L".split(","))
        self.rawblock.append("B,D,B,E,E,F".split(","))
        self.rawblock.append("S,C,D,E,A,M".split(","))
        self.rawblock.append("X,X,R,X,X,X".split(","))
        self.rawblock.append("Q,Q,Q,Q,Q,Q".split(","))
        self.wsb = WordSearchBlock(self.rawblock)

    def test_heigth_width(self):
        assert self.wsb.width == 6
        assert self.wsb.height == 6

    def test_get_coordinate(self):
        """
        Confirm that coordinates are mapped as expected
        """
        assert self.wsb.block[0][0].coord.x == 0
        assert self.wsb.block[0][0].coord.y == 0
        assert self.wsb.block[0][0].letter == "F"

        assert self.wsb.block[4][4].coord.x == 4
        assert self.wsb.block[4][4].coord.y == 4
        assert self.wsb.block[4][4].letter == "X"

        assert self.wsb.block[5][5].coord.x == 5
        assert self.wsb.block[5][5].coord.y == 5
        assert self.wsb.block[5][5].letter == "Q"

    def test_get_row(self):
        """
        Get a row from the puzzle
        """
        row = self.wsb.getRow(0)
        assert len(row) == 6
        assert row[0].letter == "F"

        row = self.wsb.getRow(5)
        assert len(row) == 6
        assert row[3].letter == "Q"

    def test_get_all_rows(self):
        """
        get all rows and confirm they all meet length and content expectations
        """
        rowtests = ["FOODXY", "AXQZUL", "BDBEEF", "SCDEAM", "XXRXXX", "QQQQQQ"]
        for i in range(6):
            row = self.wsb.getRow(i)
            assert len(row) == 6
            assert row.toString() == rowtests[i]

    def test_get_col(self):
        """
        Get a column from the puzzle
        """
        col = self.wsb.getCol(1)
        assert len(col) == 6
        assert col[3].letter == "C"

        col = self.wsb.getCol(4)
        assert len(col) == 6
        assert col[3].letter == "A"

    def test_get_all_col(self):
        """
        get all columns and confirm they all meet length and content expectations
        """
        coltests = ["FABSXQ", "OXDCXQ", "OQBDRQ", "DZEEXQ", "XUEAXQ", "YLFMXQ"]
        for i in range(6):
            col = self.wsb.getCol(i)
            assert len(col) == 6
            assert col.toString() == coltests[i]

    def test_get_fwd_slash(self):
        """
        Get a particular fwd slash out of the puzzle
        """
        fwdslash = self.wsb.getFwdSlash(3)
        assert len(fwdslash) == 4
        assert fwdslash[3].letter == "D"

    def test_get_all_fwd_slash(self):
        """
        get all fwd slashes through the block and confirm they all meet length and content expectations
        """
        lengthtest = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        fwdslashtests = ["F", "AO", "BXO", "SDQD", "XCBZX", "QXDEUY", "QREEL", "QXAF", "QXM", "QX", "Q"]
        for i in range(11):
            fwdslash = self.wsb.getFwdSlash(i)
            assert len(fwdslash) == lengthtest[i]
            assert fwdslash.toString() == fwdslashtests[i]

    def test_get_back_slash(self):
        """
        Get a single backslash
        """
        backslash = self.wsb.getBackSlash(3)
        assert len(backslash) == 4
        assert backslash[3].letter == "O"

    def test_get_all_back_slash(self):
        """
        get all fwd slashes through the block and confirm they all meet length and content expectations
        """
        lengthtest = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        backslashtests = ["Y", "LX", "FUD", "MEZO", "XAEQO", "QXEBXF", "QXDDA", "QRCB", "QXS", "QX", "Q"]

        for i in range(11):
            backslash = self.wsb.getBackSlash(i)
            assert len(backslash) == lengthtest[i]
            assert backslash.toString() == backslashtests[i]

    def test_get_all_slices(self):
        """
        get all slices through the block
        """
        slices = self.wsb.getAllSlices()
        assert len(slices) == 34

    def test_find_words(self):
        """
        get all slices through the block, I'm testing all possible solutions here
        """
        words = ["ADD", "FOOD", "BEEF", "LEER", "REEL", "FAX", "ABS", "XEEZ"]
        slices = self.wsb.getAllSlices()
        results = list()
        for slice in slices:
            for word in words:
                if word in slice:
                    results.append(slice.get_result_as_string(0))
        
        assert len(results) == 8
        assert results[0] == 'FOOD: (0,0),(1,0),(2,0),(3,0)'
        assert results[1] == 'BEEF: (2,2),(3,2),(4,2),(5,2)'
        assert results[2] == 'ABS: (0,1),(0,2),(0,3)'
        assert results[3] == 'XEEZ: (3,4),(3,3),(3,2),(3,1)'
        assert results[4] == 'LEER: (5,1),(4,2),(3,3),(2,4)'
        assert results[5] == 'REEL: (2,4),(3,3),(4,2),(5,1)'
        assert results[6] == 'FAX: (5,2),(4,3),(3,4)'
        assert results[7] == 'ADD: (0,1),(1,2),(2,3)'

class TestSlices:
    """
    set up a WordSearchBlock object that we will beat on with tests below
    """
    def setup_class(self):
        self.rawblock = list()
        #Words in here are:  FOOD, ADD, BEEF, LEER, CELERY
        #this is a rectangular block
        self.rawblock.append("F,O,O,D,X,Y,C,D".split(","))
        self.rawblock.append("A,X,Q,Z,U,L,E,F".split(","))
        self.rawblock.append("B,D,B,E,E,F,L,R".split(","))
        self.rawblock.append("S,C,D,E,A,M,E,I".split(","))
        self.rawblock.append("X,X,R,X,X,X,R,Y".split(","))
        self.rawblock.append("Q,Q,Q,Q,Q,Q,Y,Z".split(","))
        self.wsb = WordSearchBlock(self.rawblock)
    
    def test_get_fwdslash_startpos(self):
        """
        Get start positions for various forward slashes in the puzzle.
        I'm testing with a rectangular puzzle to ensure the code is robust
        enough to handle other puzzle dimensions other that square.
        """
        assert self.wsb.getFwdSlashStartPos(0) == XYCoord(0,0)
        assert self.wsb.getFwdSlashStartPos(5) == XYCoord(0,5)
        assert self.wsb.getFwdSlashStartPos(6) == XYCoord(1,5)
        assert self.wsb.getFwdSlashStartPos(7) == XYCoord(2,5)
        assert self.wsb.getFwdSlashStartPos(8) == XYCoord(3,5)
        assert self.wsb.getFwdSlashStartPos(9) == XYCoord(4,5)
        assert self.wsb.getFwdSlashStartPos(12) == XYCoord(7,5)

    def test_get_backslash_startpos(self):
        """
        testing backslash start positions as above
        """
        assert self.wsb.getBackSlashStartPos(0) == XYCoord(7,0)
        assert self.wsb.getBackSlashStartPos(5) == XYCoord(7,5)
        assert self.wsb.getBackSlashStartPos(6) == XYCoord(6,5)
        assert self.wsb.getBackSlashStartPos(7) == XYCoord(5,5)
        assert self.wsb.getBackSlashStartPos(8) == XYCoord(4,5)
        assert self.wsb.getBackSlashStartPos(9) == XYCoord(3,5)
        assert self.wsb.getBackSlashStartPos(12) == XYCoord(0,5)

    def test_slice_startval_test(self):
        """
        Rip a specific fwd slash out of the puzzle and confirm it is correct.
        """
        s = self.wsb.getFwdSlash(6)
        assert str(s) == "QREELC"


class TestInitFailures:
    def test_word_search_block_init_fail(self):
        """
        Try to init with unequal rows
        """
        rawblock = list()
        #Words in here are:  FOOD, ADD, BEEF, LEER
        rawblock.append("F,O,O,D,X,Y".split(","))
        rawblock.append("A,X,Z,U,L".split(","))
        rawblock.append("B,D,B,E,E,F".split(","))
        rawblock.append("S,C,D,E,A,M".split(","))
        rawblock.append("X,X,R,X,X,X".split(","))
        rawblock.append("Q,Q,Q,Q,Q,Q".split(","))

        with pytest.raises(ValueError) as e:
            wsb = WordSearchBlock(rawblock)
        assert "length of each row of letters must be the same" in str(e.value)       