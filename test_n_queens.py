import pytest
from n_queens import NQueens


def test_solve():
    for i in range(1, 11):
        n_queens = NQueens(i)
        if i == 2 or i == 3:
            assert n_queens.solve() == False
        else:
            assert n_queens.solve() == True


def main():
    test_solve()
    print("All tests passed.")


if __name__ == "__main__":
    main()
