class Board:
    def __init__(self, board):
        """
        Initialize the Sudoku board.

        Args:
            board (list of list of int): A 9x9 grid representing the Sudoku board.
        """
        self.board = board

    def __str__(self):
        """
        Return a string representation of the Sudoku board.
        Empty cells are represented by '*'.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str
    
    def find_empty_cell(self):
        """
        Find an empty cell in the Sudoku board.
        
        Returns:
            tuple: Row and column of the empty cell, or None if the board is full.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        """
        Check if a number is valid in the given row.
        
        Args:
            row (int): Row index.
            num (int): Number to check.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        return num not in self.board[row]
    
    def valid_in_col(self, col, num):
        """
        Check if a number is valid in the given column.
        
        Args:
            col (int): Column index.
            num (int): Number to check.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Check if a number is valid in the 3x3 square.
        
        Args:
            row (int): Row index.
            col (int): Column index.
            num (int): Number to check.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Check if a number is valid in the given cell.
        
        Args:
            empty (tuple): Row and column of the cell.
            num (int): Number to check.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])
    
    def solve(self):
        """
        Solve the Sudoku board using backtracking.
        
        Returns:
            bool: True if the board is solvable, False otherwise.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle.
    
    Args:
        board (list of list of int): A 9x9 grid representing the Sudoku board.
    
    Returns:
        list of list of int: Solved Sudoku board, or None if unsolvable.
    """
    gameboard = Board(board)
    print(f"Puzzle to solve:\n{gameboard}")
    if gameboard.solve():
        print(f"Solved puzzle:\n{gameboard}")
        return gameboard.board    
    else:
        print("The provided puzzle is unsolvable.")
        return None