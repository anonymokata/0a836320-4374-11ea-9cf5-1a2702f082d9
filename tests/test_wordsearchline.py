import pytest
from XYLines import CoordinateProducer, Direction, LineType
from XYCoord import XYCoord
from WordSearchLine import WordSearchLine
from WordSearchLetter import WordSearchLetter


class TestWordSearchLine_BasicTests:
    def test_init(self):
        line = [WordSearchLetter(x, XYCoord(0, 0)) for x in "ABCHELLOXYZ"]
        wsl = WordSearchLine(line)
        assert isinstance(wsl, WordSearchLine)

    def test_getstring(self):
        line = [WordSearchLetter(x, XYCoord(0, 0)) for x in "ABCHELLOXYZ"]
        wsl = WordSearchLine(line)
        assert wsl.toString() == "ABCHELLOXYZ"

    def test_membership(self):
        """
        check that the word "HELLO" is discovered in the line in forward direction
        using "in" operator is pythonic way of testing for membership
        """
        line = [WordSearchLetter(x, XYCoord(0, 0)) for x in "ABCHELLOXYZ"]
        wsl = WordSearchLine(line)
        assert "HELLO" in wsl
        assert wsl.matches[0].direction == Direction.Forward

    def test_membership_backwards(self):
        """
        check that the word "OLLEH" is discovered in the line in backwards direction
        """
        line = [WordSearchLetter(x, XYCoord(0, 0)) for x in "ABCHELLOXYZ"]
        wsl = WordSearchLine(line)
        assert "OLLEH" in wsl
        assert wsl.matches[0].direction == Direction.Backward

    def test_nomembership(self):
        """
        test that the word "FISH" is NOT discovered in the line and direction is not set
        """
        line = [WordSearchLetter(x, XYCoord(0, 0)) for x in "ABCHELLOXYZ"]
        wsl = WordSearchLine(line)
        assert "FISH" not in wsl
        assert len(wsl.matches) == 0


class TestWordSearchLine_SCOTTY:
    def setup_class(self):
        """
        Real test case from the kata description
        """
        row = "S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F"
        rownum = 5

        #need to create a WordSeachLine with the appropriate coordinates, will do this by creating two lists
        #a list containing each letter and a list containing XYCoord objects, will zip these together and use
        #to init a "line" of WordSearchLetter objects

        row = row.split(",")  #there's my list of letters
        coords = [XYCoord(x,rownum) for x in range(len(row))]  #there's my list of coords

        self.line = [WordSearchLetter(let, coord) for let,coord in zip(row,coords)]  #there's my 'line' of WordSearchLetter objects

        assert isinstance(self.line, list)

    def test_SCOTTY_ismember(self):
        wsl = WordSearchLine(self.line)
        assert wsl.toString() == "SCOTTYKZREPPXPF"
        assert "SCOTTY" in wsl

    def test_SCOTTY_getmatches(self):
        """
        Confirm results indicate start position, length, and direciton
        """
        wsl = WordSearchLine(self.line)
        if "SCOTTY" in wsl:
            assert wsl.matches[0].startpos == 0
            assert wsl.matches[0].direction == Direction.Forward
            assert wsl.matches[0].length == 6

    def test_SCOTTY_getmatches_with_search_method(self):
        """
        Confirming that the search method is just as good as the 'in' operator
        """
        wsl = WordSearchLine(self.line)
        if wsl.search("SCOTTY") == True:
            assert wsl.matches[0].startpos == 0
            assert wsl.matches[0].direction == Direction.Forward
            assert wsl.matches[0].length == 6

    def test_SCOTTY_get_answer(self):
        wsl = WordSearchLine(self.line)
        if wsl.search("SCOTTY") == True:
            assert wsl.get_result_as_string(0) == "SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)"


class TestWordSearchLine_KIRK:
    def setup_class(self):
        """
        Real test case from kata description, although this one is the word found backwards
        see SCOTTY test case for description of what is going on here
        """
        row = "O,K,R,I,K,A,M,M,R,M,F,B,A,P,P"
        rownum = 7

        row = row.split(",")  #there's my list of letters
        coords = [XYCoord(x,rownum) for x in range(len(row))]  #there's my list of coords

        self.line = [WordSearchLetter(let, coord) for let,coord in zip(row,coords)]  #there's my 'line' of WordSearchLetter objects

        assert isinstance(self.line, list)


    def test_KIRK_ismember(self):
        wsl = WordSearchLine(self.line)
        assert wsl.toString() == "OKRIKAMMRMFBAPP"
        assert "KIRK" in wsl

    def test_KIRK_getmatches(self):
        """
        Confirm results indicate start position, length, and direciton
        """
        wsl = WordSearchLine(self.line)
        if "KIRK" in wsl:
            assert wsl.matches[0].startpos == 10
            assert wsl.matches[0].direction == Direction.Backward
            assert wsl.matches[0].length == 4

    def test_KIRK_getmatches_with_search_method(self):
        """
        Confirming that the search method is just as good as the 'in' operator
        """
        wsl = WordSearchLine(self.line)
        if wsl.search("KIRK") == True:
            assert wsl.matches[0].startpos == 10
            assert wsl.matches[0].direction == Direction.Backward
            assert wsl.matches[0].length == 4 

    def test_KIRK_get_answer(self):
        wsl = WordSearchLine(self.line)
        if wsl.search("KIRK") == True:
            assert wsl.get_result_as_string(0) == "KIRK: (4,7),(3,7),(2,7),(1,7)"