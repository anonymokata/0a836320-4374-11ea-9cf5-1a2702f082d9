import pytest
from XYCoord import XYCoord


class TestXYCoord:
    def test_coord(self):
        c = XYCoord(5,9)
        assert c.x == 5
        assert c.y == 9

    def test_coord_string_conversion(self):
        c = XYCoord(7, 9)
        assert str(c) == "(7,9)"

    def test_coord_invalid_argument(self):
        with pytest.raises(ValueError) as e:
            c = XYCoord(1.1, 0.2)
        assert "must be integers" in str(e.value)