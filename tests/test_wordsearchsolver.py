import pytest
from WordSearchLetter import WordSearchLetter
from XYCoord import XYCoord
from WordSearchSolver import WordSearchSolver

class TestWordSearchSolver:

    def test_word_search_solver_failure_problem(self):
        with pytest.raises(ValueError) as e:
            WordSearchSolver('tests/kata_failure_testcase.txt')
        assert "doesn't contain a comma anywhere" in str(e.value)

    def test_word_search_solver_kata_problem(self):
        wss = WordSearchSolver('tests/kata_testcase.txt')
        assert wss.solution() == """BONES: (0,6),(0,7),(0,8),(0,9),(0,10)
KHAN: (5,9),(5,8),(5,7),(5,6)
KIRK: (4,7),(3,7),(2,7),(1,7)
SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)
SULU: (3,3),(2,2),(1,1),(0,0)
UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)"""