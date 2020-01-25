import pytest
from WordSearch import LineType, WordSearchLine, SearchDir, XYCoord

class TestXYCoord:
    def test_coord(self):
        c = XYCoord(5,9)
        assert c.x == 5
        assert c.y == 9
        assert str(c) == "(5,9)"


class TestWordSearchLine_BasicTests:
    def test_init(self):
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert wsl.line == "ABCHELLOXYZ"
        assert wsl.linetype == LineType.Row
        assert wsl.startcoord.x == 0
        assert wsl.startcoord.y == 0

    def test_membership(self):
        """
        check that the word "HELLO" is discovered in the line in forward direction
        using "in" operator is pythonic way of testing for membership
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert "HELLO" in wsl
        assert wsl.searchdirection == SearchDir.Forward

    def test_membership_backwards(self):
        """
        check that the word "OLLEH" is discovered in the line in backwards direction
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert "OLLEH" in wsl
        assert wsl.searchdirection == SearchDir.Backward

    def test_nomembership(self):
        """
        test that the word "FISH" is NOT discovered in the line and direction is not set
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert "FISH" not in wsl
        assert wsl.searchdirection == None


class TestWordSearchLine_RowTests:
    """
    tests specifically when the line is a 'row' type that coordinates are returned properly
    """
    def test_row_coordlist_forward(self):
        """
        Testing for the occurrence of HELLO in string
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert "HELLO" in wsl
        assert wsl.searchdirection == SearchDir.Forward
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(3,0)"
        assert str(wsl.coords[1]) == "(4,0)"
        assert str(wsl.coords[2]) == "(5,0)"
        assert str(wsl.coords[3]) == "(6,0)"
        assert str(wsl.coords[4]) == "(7,0)"

    def test_row_coordlist_backward(self):
        """
        Testing for the occurrence of OLLEH in string
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert "OLLEH" in wsl
        assert wsl.searchdirection == SearchDir.Backward
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(7,0)"
        assert str(wsl.coords[1]) == "(6,0)"
        assert str(wsl.coords[2]) == "(5,0)"
        assert str(wsl.coords[3]) == "(4,0)"
        assert str(wsl.coords[4]) == "(3,0)"