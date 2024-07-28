import tkinter as tk

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

# tkinter setup
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)
#root.iconbitmap("./assets/sudoku.ico")
root.mainloop()