import pytest
from XYLines import CoordinateProducer, Direction, XYCoord, LineType
from WordSearch import WordSearchLine


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
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir

    def test_membership_backwards(self):
        """
        check that the word "OLLEH" is discovered in the line in backwards direction
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Row, XYCoord(0,0))
        assert "OLLEH" in wsl
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir

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
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir
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
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir
        assert len(wsl.coords) == 5   #length of word "OLLEH"
        assert str(wsl.coords[0]) == "(7,0)"
        assert str(wsl.coords[1]) == "(6,0)"
        assert str(wsl.coords[2]) == "(5,0)"
        assert str(wsl.coords[3]) == "(4,0)"
        assert str(wsl.coords[4]) == "(3,0)"

    def test_row_coordlist_forward_word_at_start(self):
        """
        Testing for the occurrence of HELLO in string when placed at start of string
        """
        wsl = WordSearchLine("HELLOXYZABC", LineType.Row, XYCoord(0,0))
        assert "HELLO" in wsl
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(0,0)"
        assert str(wsl.coords[1]) == "(1,0)"
        assert str(wsl.coords[2]) == "(2,0)"
        assert str(wsl.coords[3]) == "(3,0)"
        assert str(wsl.coords[4]) == "(4,0)"

    def test_row_coordlist_backward_word_at_end(self):
        """
        Testing for the occurrence of FOOBAR in string when it is placed at end of string
        """
        wsl = WordSearchLine("ABCXYZRABOOF", LineType.Row, XYCoord(0,0))
        assert "FOOBAR" in wsl
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir
        assert len(wsl.coords) == 6   #length of word "FOOBAR"
        assert str(wsl.coords[0]) == "(11,0)"
        assert str(wsl.coords[1]) == "(10,0)"
        assert str(wsl.coords[2]) == "(9,0)"
        assert str(wsl.coords[3]) == "(8,0)"
        assert str(wsl.coords[4]) == "(7,0)"
        assert str(wsl.coords[5]) == "(6,0)"


class TestWordSearchLine_ColTests:
    """
    tests specifically when the line is a 'column' type that coordinates are returned properly
    """
    def test_col_coordlist_forward(self):
        """
        Testing for the occurrence of HELLO in string
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Column, XYCoord(0,0))
        assert "HELLO" in wsl
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(0,3)"
        assert str(wsl.coords[1]) == "(0,4)"
        assert str(wsl.coords[2]) == "(0,5)"
        assert str(wsl.coords[3]) == "(0,6)"
        assert str(wsl.coords[4]) == "(0,7)"

    def test_col_coordlist_backward(self):
        """
        Testing for the occurrence of OLLEH in string
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Column, XYCoord(0,0))
        assert "OLLEH" in wsl
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir
        assert len(wsl.coords) == 5   #length of word "OLLEH"
        assert str(wsl.coords[0]) == "(0,7)"
        assert str(wsl.coords[1]) == "(0,6)"
        assert str(wsl.coords[2]) == "(0,5)"
        assert str(wsl.coords[3]) == "(0,4)"
        assert str(wsl.coords[4]) == "(0,3)"

    def test_col_coordlist_forward_word_at_start(self):
        """
        Testing for the occurrence of HELLO in string when placed at start of string
        """
        wsl = WordSearchLine("HELLOXYZABC", LineType.Column, XYCoord(0,0))
        assert "HELLO" in wsl
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(0,0)"
        assert str(wsl.coords[1]) == "(0,1)"
        assert str(wsl.coords[2]) == "(0,2)"
        assert str(wsl.coords[3]) == "(0,3)"
        assert str(wsl.coords[4]) == "(0,4)"

    def test_col_coordlist_backward_word_at_end(self):
        """
        Testing for the occurrence of FOOBAR in string when it is placed at end of string
        """
        wsl = WordSearchLine("ABCXYZRABOOF", LineType.Column, XYCoord(0,0))
        assert "FOOBAR" in wsl
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir
        assert len(wsl.coords) == 6   #length of word "FOOBAR"
        assert str(wsl.coords[0]) == "(0,11)"
        assert str(wsl.coords[1]) == "(0,10)"
        assert str(wsl.coords[2]) == "(0,9)"
        assert str(wsl.coords[3]) == "(0,8)"
        assert str(wsl.coords[4]) == "(0,7)"
        assert str(wsl.coords[5]) == "(0,6)"



class TestWordSearchLine_FwdSlashTests:
    """
    tests specifically when the line is a 'forwardslash' type that coordinates are returned properly
    """
    def test_col_coordlist_forward(self):
        """
        Testing for the occurrence of HELLO in string
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Forwardslash, XYCoord(0,11))
        assert "HELLO" in wsl
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(3,8)"
        assert str(wsl.coords[1]) == "(4,7)"
        assert str(wsl.coords[2]) == "(5,6)"
        assert str(wsl.coords[3]) == "(6,5)"
        assert str(wsl.coords[4]) == "(7,4)"

    def test_col_coordlist_backward(self):
        """
        Testing for the occurrence of OLLEH in string
        """
        wsl = WordSearchLine("ABCHELLOXYZ", LineType.Forwardslash, XYCoord(8,0))
        assert "OLLEH" in wsl
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir
        assert len(wsl.coords) == 5   #length of word "OLLEH"
        assert str(wsl.coords[0]) == "(0,7)"
        assert str(wsl.coords[1]) == "(0,6)"
        assert str(wsl.coords[2]) == "(0,5)"
        assert str(wsl.coords[3]) == "(0,4)"
        assert str(wsl.coords[4]) == "(0,3)"

    def test_col_coordlist_forward_word_at_start(self):
        """
        Testing for the occurrence of HELLO in string when placed at start of string
        """
        wsl = WordSearchLine("HELLOXYZABC", LineType.Forwardslash, XYCoord(0,0))
        assert "HELLO" in wsl
        assert wsl.searchdirection == Direction.Forward   #word was found in forward search dir
        assert len(wsl.coords) == 5   #length of word "HELLO"
        assert str(wsl.coords[0]) == "(0,0)"
        assert str(wsl.coords[1]) == "(0,1)"
        assert str(wsl.coords[2]) == "(0,2)"
        assert str(wsl.coords[3]) == "(0,3)"
        assert str(wsl.coords[4]) == "(0,4)"

    def test_col_coordlist_backward_word_at_end(self):
        """
        Testing for the occurrence of FOOBAR in string when it is placed at end of string
        """
        wsl = WordSearchLine("ABCXYZRABOOF", LineType.Forwardslash, XYCoord(0,0))
        assert "FOOBAR" in wsl
        assert wsl.searchdirection == Direction.Backward   #word was found in backward search dir
        assert len(wsl.coords) == 6   #length of word "FOOBAR"
        assert str(wsl.coords[0]) == "(0,11)"
        assert str(wsl.coords[1]) == "(0,10)"
        assert str(wsl.coords[2]) == "(0,9)"
        assert str(wsl.coords[3]) == "(0,8)"
        assert str(wsl.coords[4]) == "(0,7)"
        assert str(wsl.coords[5]) == "(0,6)"