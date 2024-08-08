import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

    def create_grid(self):
        """Create a 9x9 grid of entry widgets for the Sudoku board."""
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center', borderwidth=2, relief='solid')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.cells[i][j] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku, font=('Arial', 14))
        solve_button.grid(row=9, column=4, columnspan=1, pady=20)

    def get_board(self):
        """Retrieve the current board state from the grid entries."""
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                self.board[i][j] = int(value) if value.isdigit() else 0

    def update_grid(self):
        """Update the grid with the solved board values."""
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(self.board[i][j]))

    def is_valid(self, num, pos):
        """Check if placing a number in a position is valid."""
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def find_empty(self):
        """Find the next empty cell on the board."""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):
        """Solve the Sudoku board using backtracking."""
        empty = self.find_empty()
        if not empty:
            return True
        else:
            row, col = empty

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def solve_sudoku(self):
        """Handle the Solve button click event."""
        self.get_board()
        if self.solve():
            self.update_grid()
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
