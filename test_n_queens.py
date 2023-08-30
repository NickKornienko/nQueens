import pytest
from n_queens import NQueens

def test_solve():
    n_queens = NQueens(4)
    assert n_queens.solve() == True

def test_is_safe():
    n_queens = NQueens(4)
    assert n_queens.is_safe(n_queens.board, 0, 0) == True
