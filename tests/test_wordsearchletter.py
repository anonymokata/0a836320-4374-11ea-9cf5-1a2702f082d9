import pytest
from WordSearchLetter import WordSearchLetter
from XYCoord import XYCoord


class Test_WordSearchLetter:
    def test_wordsearchletter_works(self):
        """
        Basic test of the WordSearchLetter class
        """
        l = list()
        l.append(WordSearchLetter("A", XYCoord(0, 0)))
        assert str(l[0]) == "A"
        assert l[0].coord.x == 0
        assert l[0].coord.y == 0

    def test_wordsearchletter_non_alpha_fail(self):
        """
        Can't init with anything other than a capital letter
        """
        with pytest.raises(ValueError) as e:
            WordSearchLetter("1", XYCoord(0, 0))
        assert "must be a capital letter" in str(e.value)

    def test_wordsearchletter_non_int_coordinate_fail(self):
        """
        Can't init coordinates with anything other than positive integers
        """
        with pytest.raises(ValueError) as e:
            WordSearchLetter("A", XYCoord(0, -2))
        assert "must be zero or positive integers" in str(e.value)

        with pytest.raises(ValueError) as e:
            WordSearchLetter("A", XYCoord(-2, 0))
        assert "must be zero or positive integers" in str(e.value)

    def test_wordsearchletter_more_than_one_letter_fail(self):
        """
        Can't init letter with more than one character
        """
        with pytest.raises(ValueError) as e:
            WordSearchLetter("ABCDE", XYCoord(1, 0))
        assert "with a single letter" in str(e.value)

    def test_wordsearchletter_get_coord_string(self):
        """
        Can't init letter with more than one character
        """
        l = WordSearchLetter("A", XYCoord(0, 0))
        assert str(l.coord) == "(0,0)"

        l = WordSearchLetter("A", XYCoord(1, 2))
        assert str(l.coord) == "(1,2)"