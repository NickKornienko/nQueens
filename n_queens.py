from typing import List


class NQueens:
    def __init__(self, size: int):
        self.size = size
        self.board = [[0]*size for _ in range(size)]

    def solve(self):
        if not self.solve_n_queens_util(self.board, 0):
            print("Solution does not exist")
            return False
        self.print_solution(self.board)
        return True

    def is_safe(self, board: List[List[int]], row: int, col: int):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.size, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_n_queens_util(self, board: List[List[int]], col: int):
        if col >= self.size:
            return True
        for i in range(self.size):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                if self.solve_n_queens_util(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    def print_solution(self, board: List[List[int]]):
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j], end=" ")
            print()


def main():
    # take user input and make sure it is an integer between 1 - 10, then create a new NQueens object of that size
    while True:
        try:
            size = int(input("Enter a number between 1 and 10: "))
            if size < 1 or size > 10:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Try again.")
    n_queens = NQueens(size)
    n_queens.solve()


if __name__ == "__main__":
    main()
