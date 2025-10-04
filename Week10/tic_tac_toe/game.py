"""
game.py
Author: Ronald Ephraim Tiangson
Description:
    Defines the Game class that manages the Tic-Tac-Toe gameplay loop,
    turn switching, win/draw detection, and board interaction.

Note:
    A coordinate guide is displayed when the game starts to show
    valid move positions (e.g. 11, 12, 13 ... 33).
"""

from typing import List, Optional
from board import Board
from player import Player


class Game:
    """Manage the flow and logic of the Tic-Tac-Toe game."""

    def __init__(self, player1: Player, player2: Player) -> None:
        """Initialize the game with two players."""
        self.board = Board()
        self.players: List[Player] = [player1, player2]
        self.current_index = 0

        # Display coordinate reference once at game start
        self.display_reference_board()

    def display_reference_board(self) -> None:
        """Display coordinate guide for player moves (e.g., 11, 12, 13)."""
        print("\n Coordinate Guide:")
        for i in range(1, self.board.size + 1):
            row = " | ".join(f"{i}{j}" for j in range(1, self.board.size + 1))
            print(f" {row} ")
            if i < self.board.size:
                print("---+" * (self.board.size - 1) + "---")
        print()

    def switch_player(self) -> None:
        """Switch to the next player's turn."""
        self.current_index = 1 - self.current_index

    def play_turn(self) -> None:
        """Execute one player's turn."""
        current_player = self.players[self.current_index]
        self.board.display()
        current_player.make_move(self.board)

    def is_game_over(self) -> bool:
        """Return True if the game has a winner or is a draw."""
        return self.board.check_winner() is not None or self.board.is_full()

    def get_winner(self) -> Optional[Player]:
        """Return the winner Player object, or None."""
        winner_symbol = self.board.check_winner()
        if winner_symbol:
            for player in self.players:
                if player.symbol == winner_symbol:
                    return player
        return None

    def run(self) -> None:
        """Main gameplay loop."""
        print("\nWelcome to Tic-Tac-Toe!\n")
        while not self.is_game_over():
            self.play_turn()
            winner = self.get_winner()
            if winner:
                self.board.display()
                print(f" {winner.name} wins!")
                return
            self.switch_player()

        self.board.display()
        print("It's a draw!")
