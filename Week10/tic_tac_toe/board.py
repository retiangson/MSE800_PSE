"""
board.py
Author: Ronald Ephraim Tiangson
Description:
    Defines the Board class for the Tic-Tac-Toe game.
    Handles grid creation, updates, winner checks, and display.
"""

from typing import List, Optional


class Board:
    """Represent the Tic-Tac-Toe board and its operations."""

    def __init__(self, size: int = 3) -> None:
        """Initialize the board with a given size."""
        self.size = size
        self.grid: List[List[str]] = [[" " for _ in range(size)] for _ in range(size)]

    def display(self) -> None:
        """Print the current board to the console."""
        print()
        for i in range(self.size):
            row = " | ".join(self.grid[i])
            print(f" {row} ")
            if i < self.size - 1:
                print("---+" * (self.size - 1) + "---")
        print()

    def update_cell(self, row: int, col: int, symbol: str) -> bool:
        """Update a cell if it's empty. Return True if successful."""
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        print("Cell already taken. Try again.")
        return False

    def is_full(self) -> bool:
        """Return True if no empty cells remain."""
        return all(cell != " " for row in self.grid for cell in row)

    def check_winner(self) -> Optional[str]:
        """Return the symbol of the winner, or None if no winner."""
        lines = []

        # Rows and columns
        for i in range(self.size):
            lines.append(self.grid[i])
            lines.append([self.grid[j][i] for j in range(self.size)])

        # Diagonals
        lines.append([self.grid[i][i] for i in range(self.size)])
        lines.append([self.grid[i][self.size - i - 1] for i in range(self.size)])

        for line in lines:
            if line.count(line[0]) == self.size and line[0] != " ":
                return line[0]
        return None

    def reset(self) -> None:
        """Reset the board to its initial empty state."""
        self.grid = [[" " for _ in range(self.size)] for _ in range(self.size)]
