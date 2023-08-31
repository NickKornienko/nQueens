The core classes, functions, and methods that will be necessary are:

1. `NQueens` class: This class will encapsulate the logic for solving the n-queens problem.
    - `__init__(self, size: int)`: Initializes an instance of the `NQueens` class.
    - `solve(self)`: Solves the n-queens problem.
    - `is_safe(self, board: List[List[int]], row: int, col: int)`: Checks if a queen can be placed at the given position.
    - `solve_n_queens_util(self, board: List[List[int]], col: int)`: Utility method to solve the n-queens problem.
    - `print_solution(self, board: List[List[int]])`: Prints the solution.

2. `test_n_queens.py`: This file will contain the unit tests for the `NQueens` class.
    - `test_solve()`: Tests the `solve` method of the `NQueens` class.

Now, let's write the code for each file.

`n_queens.py`
