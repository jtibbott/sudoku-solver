import tkinter as tk
from tkinter import messagebox
from copy import deepcopy
from SudokuSolver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("450x500")
        self.root.resizable(False, False)
        
        self.board = [[0] * 9 for _ in range(9)]
        self.initial_board = deepcopy(self.board)
        self.undo_stack = []
        
  
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()