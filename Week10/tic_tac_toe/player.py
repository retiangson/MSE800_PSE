"""
player.py
Author: Ronald Ephraim Tiangson
Description:
    Defines the Player class that represents a Tic-Tac-Toe player.
    Handles move input and validation.

Note:
    Players should now enter their move as two digits with no space or comma.
    For example:
        11 → row 1, column 1
        12 → row 1, column 2
        33 → row 3, column 3
"""

from board import Board


class Player:
    """Represent a player in the Tic-Tac-Toe game."""

    def __init__(self, name: str, symbol: str) -> None:
        """Initialize player with a name and symbol."""
        self.name = name
        self.symbol = symbol

    def make_move(self, board: Board) -> None:
        """
        Ask the player for their move until a valid one is made.

        Accepts input as two digits with no space or comma:
            '11' → row 1, col 1
            '23' → row 2, col 3
        """
        while True:
            move = input(
                f"{self.name} ({self.symbol}), enter your move as two digits (rowcol, e.g. 13): "
            ).strip()

            # Validate: must be exactly two digits
            if not (len(move) == 2 and move.isdigit()):
                print("Invalid format. Enter exactly two digits (e.g. 13 for row1 col3).")
                continue

            row, col = int(move[0]) - 1, int(move[1]) - 1

            # Range check
            if 0 <= row < board.size and 0 <= col < board.size:
                if board.update_cell(row, col, self.symbol):
                    break
                # Board.update_cell prints cell taken if needed
            else:
                print("Invalid range. Enter numbers between 1 and 3 for both row and column.")
