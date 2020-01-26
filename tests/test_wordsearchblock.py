import pytest
from WordSearchLetter import WordSearchLetter
from WordSearchLine import WordSearchLine
from WordSearchBlock import WordSearchBlock

class Test_WordSearchBlock:
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
        row = self.wsb.getRow(0)
        assert len(row) == 6
        assert row[0].letter == "F"

        row = self.wsb.getRow(5)
        assert len(row) == 6
        assert row[3].letter == "Q"

    def test_get_all_rows(self):
        rowtests = ["FOODXY", "AXQZUL", "BDBEEF", "SCDEAM", "XXRXXX", "QQQQQQ"]
        for i in range(6):
            row = self.wsb.getRow(i)
            assert len(row) == 6
            assert row.toString() == rowtests[i]

    def test_get_col(self):
        col = self.wsb.getCol(1)
        assert len(col) == 6
        assert col[3].letter == "C"

        col = self.wsb.getCol(4)
        assert len(col) == 6
        assert col[3].letter == "A"

    def test_get_all_col(self):
        coltests = ["FABSXQ", "OXDCXQ", "OQBDRQ", "DZEEXQ", "XUEAXQ", "YLFMXQ"]
        for i in range(6):
            col = self.wsb.getCol(i)
            assert len(col) == 6
            assert col.toString() == coltests[i]

    def test_get_fwd_slash(self):
        fwdslash = self.wsb.getFwdSlash(3)
        assert len(fwdslash) == 4
        assert fwdslash[3].letter == "D"

    def test_get_all_fwd_slash(self):
        """
        get all fwd slashes through the block and confirm they all meet length expectations
        """
        lengthtest = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        fwdslashtests = ["F", "AO", "BXO", "SDQD", "XCBZX", "QXDEUY", "QREEL", "QXAF", "QXM", "QX", "Q"]
        for i in range(11):
            fwdslash = self.wsb.getFwdSlash(i)
            assert len(fwdslash) == lengthtest[i]
            assert fwdslash.toString() == fwdslashtests[i]

    def test_get_back_slash(self):
        backslash = self.wsb.getBackSlash(3)
        assert len(backslash) == 4
        assert backslash[3].letter == "O"

    def test_get_all_back_slash(self):
        """
        get all fwd slashes through the block and confirm they all meet length expectations
        """
        lengthtest = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        backslashtests = ["Y", "LX", "FUD", "MEZO", "XAEQO", "QXEBXF", "QXDDA", "QRCB", "QXS", "QX", "Q"]

        for i in range(11):
            backslash = self.wsb.getBackSlash(i)
            assert len(backslash) == lengthtest[i]
            assert backslash.toString() == backslashtests[i]

    