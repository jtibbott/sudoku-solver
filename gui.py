import tkinter as tk
from tkinter import messagebox
from copy import deepcopy
from SudokuSolver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("360x420")
        self.root.resizable(False, False)

        self.board = [[0] * 9 for _ in range(9)]
        self.initial_board = deepcopy(self.board)
        self.undo_stack = []

        self.create_widgets()

    def create_widgets(self):
        self.entries = []
        for row in range(9):
            row_entries = []
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=row, column=col, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        self.solve_button.grid(row=9, column=1, columnspan=2, pady=10, padx=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.grid(row=9, column=3, columnspan=2, pady=10, padx=10)

        self.undo_button = tk.Button(self.root, text="Undo", command=self.undo)
        self.undo_button.grid(row=9, column=5, columnspan=2, pady=10, padx=10)

    def solve(self):
        self.update_board_from_entries()
        self.undo_stack.append(deepcopy(self.board))
        solved_board = solve_sudoku(deepcopy(self.board))
        if solved_board:
            self.board = solved_board
            self.update_entries_from_board()
        else:
            messagebox.showerror("Error", "The provided puzzle is unsolvable.")

    def reset(self):
        self.board = deepcopy(self.initial_board)
        self.update_entries_from_board()

    def undo(self):
        if self.undo_stack:
            self.board = self.undo_stack.pop()
            self.update_entries_from_board()
        else:
            messagebox.showwarning("Warning", "No actions to undo.")

    def update_board_from_entries(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                self.board[row][col] = int(value) if value.isdigit() else 0

    def update_entries_from_board(self):
        for row in range(9):
            for col in range(9):
                value = self.board[row][col]
                self.entries[row][col].delete(0, tk.END)
                if value != 0:
                    self.entries[row][col].insert(0, str(value))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
