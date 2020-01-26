import pytest
from XYLines import CoordinateProducer, Direction, XYCoord, LineType
from WordSearch import WordSearchLine

class TestCoordinateProducer_RowTests:
    def test_getcoords_rowtype_forwardsearch_length_5_start_0_0(self):
        cp = CoordinateProducer(XYCoord(0,0), LineType.Row, Direction.Forward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,0)"
        assert str(coords[1]) == "(1,0)"
        assert str(coords[2]) == "(2,0)"
        assert str(coords[3]) == "(3,0)"
        assert str(coords[4]) == "(4,0)"

    def test_getcoords_rowtype_backwardsearch_length_5_start_5_0(self):
        cp = CoordinateProducer(XYCoord(5,0), LineType.Row, Direction.Backward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(5,0)"
        assert str(coords[1]) == "(4,0)"
        assert str(coords[2]) == "(3,0)"
        assert str(coords[3]) == "(2,0)"
        assert str(coords[4]) == "(1,0)"

    def test_getcoords_rowtype_forwardsearch_length_5_start_0_0_offset_2(self):
        cp = CoordinateProducer(XYCoord(0,0), LineType.Row, Direction.Forward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(2,0)"
        assert str(coords[1]) == "(3,0)"
        assert str(coords[2]) == "(4,0)"
        assert str(coords[3]) == "(5,0)"
        assert str(coords[4]) == "(6,0)"

    def test_getcoords_rowtype_backwardsearch_length_5_start_10_0_offset_2(self):
        cp = CoordinateProducer(XYCoord(10,0), LineType.Row, Direction.Backward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(8,0)"
        assert str(coords[1]) == "(7,0)"
        assert str(coords[2]) == "(6,0)"
        assert str(coords[3]) == "(5,0)"
        assert str(coords[4]) == "(4,0)"

class TestCoordinateProducer_ColTests:
    def test_getcoords_rowtype_forwardsearch_length_5_start_0_0(self):
        cp = CoordinateProducer(XYCoord(0,0), LineType.Column, Direction.Forward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,0)"
        assert str(coords[1]) == "(0,1)"
        assert str(coords[2]) == "(0,2)"
        assert str(coords[3]) == "(0,3)"
        assert str(coords[4]) == "(0,4)"

    def test_getcoords_rowtype_backwardsearch_length_5_start_0_5(self):
        cp = CoordinateProducer(XYCoord(0,5), LineType.Column, Direction.Backward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,5)"
        assert str(coords[1]) == "(0,4)"
        assert str(coords[2]) == "(0,3)"
        assert str(coords[3]) == "(0,2)"
        assert str(coords[4]) == "(0,1)"

    def test_getcoords_rowtype_forwardsearch_length_5_start_0_0_offset_2(self):
        cp = CoordinateProducer(XYCoord(0,0), LineType.Column, Direction.Forward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,2)"
        assert str(coords[1]) == "(0,3)"
        assert str(coords[2]) == "(0,4)"
        assert str(coords[3]) == "(0,5)"
        assert str(coords[4]) == "(0,6)"

    def test_getcoords_rowtype_backwardsearch_length_5_start_0_10_offset_2(self):
        cp = CoordinateProducer(XYCoord(0,10), LineType.Column, Direction.Backward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,8)"
        assert str(coords[1]) == "(0,7)"
        assert str(coords[2]) == "(0,6)"
        assert str(coords[3]) == "(0,5)"
        assert str(coords[4]) == "(0,4)"

class TestCoordinateProducer_ForwardSlashTests:
    def test_getcoords_forwardslash_forwardsearch_length_5_start_0_5(self):
        cp = CoordinateProducer(XYCoord(0,5), LineType.Forwardslash, Direction.Forward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,5)"
        assert str(coords[1]) == "(1,4)"
        assert str(coords[2]) == "(2,3)"
        assert str(coords[3]) == "(3,2)"
        assert str(coords[4]) == "(4,1)"

    def test_getcoords_forwardslash_backwardsearch_length_5_start_5_0(self):
        cp = CoordinateProducer(XYCoord(5,0), LineType.Forwardslash, Direction.Backward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(5,0)"
        assert str(coords[1]) == "(4,1)"
        assert str(coords[2]) == "(3,2)"
        assert str(coords[3]) == "(2,3)"
        assert str(coords[4]) == "(1,4)"

    def test_getcoords_forwardslash_forwardsearch_length_5_start_0_10_offset_2(self):
        cp = CoordinateProducer(XYCoord(0,10), LineType.Forwardslash, Direction.Forward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(2,8)"
        assert str(coords[1]) == "(3,7)"
        assert str(coords[2]) == "(4,6)"
        assert str(coords[3]) == "(5,5)"
        assert str(coords[4]) == "(6,4)"

    def test_getcoords_forwardslash_backwardsearch_length_5_start_10_0_offset_2(self):
        cp = CoordinateProducer(XYCoord(10,0), LineType.Forwardslash, Direction.Backward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(8,2)"
        assert str(coords[1]) == "(7,3)"
        assert str(coords[2]) == "(6,4)"
        assert str(coords[3]) == "(5,5)"
        assert str(coords[4]) == "(4,6)"


class TestCoordinateProducer_BackSlashTests:
    def test_getcoords_backslash_forwardsearch_length_5_start_0_0(self):
        cp = CoordinateProducer(XYCoord(0,0), LineType.Backslash, Direction.Forward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(0,0)"
        assert str(coords[1]) == "(1,1)"
        assert str(coords[2]) == "(2,2)"
        assert str(coords[3]) == "(3,3)"
        assert str(coords[4]) == "(4,4)"

    def test_getcoords_backslash_backwardsearch_length_5_start_5_5(self):
        cp = CoordinateProducer(XYCoord(5,5), LineType.Backslash, Direction.Backward, 5)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(5,5)"
        assert str(coords[1]) == "(4,4)"
        assert str(coords[2]) == "(3,3)"
        assert str(coords[3]) == "(2,2)"
        assert str(coords[4]) == "(1,1)"

    def test_getcoords_backslash_forwardsearch_length_5_start_0_0_offset_2(self):
        cp = CoordinateProducer(XYCoord(0,0), LineType.Backslash, Direction.Forward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(2,2)"
        assert str(coords[1]) == "(3,3)"
        assert str(coords[2]) == "(4,4)"
        assert str(coords[3]) == "(5,5)"
        assert str(coords[4]) == "(6,6)"

    def test_getcoords_backslash_backwardsearch_length_5_start_10_10_offset_2(self):
        cp = CoordinateProducer(XYCoord(10,10), LineType.Backslash, Direction.Backward, 5, 2)
        coords = cp.getCoords()
        assert len(coords) == 5
        assert str(coords[0]) == "(8,8)"
        assert str(coords[1]) == "(7,7)"
        assert str(coords[2]) == "(6,6)"
        assert str(coords[3]) == "(5,5)"
        assert str(coords[4]) == "(4,4)"