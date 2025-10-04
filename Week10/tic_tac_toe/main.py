"""
main.py
Author: Ronald Ephraim Tiangson
Description:
    Entry point for the Tic-Tac-Toe game.
    Demonstrates top-down design, modularization, and PEP8 compliance.
"""

from player import Player
from game import Game


def main() -> None:
    """Main entry point for running the Tic-Tac-Toe game."""
    print("Tic-Tac-Toe Game\n")
    player1 = Player(input("Enter name for Player 1 (X): "), "X")
    player2 = Player(input("Enter name for Player 2 (O): "), "O")

    game = Game(player1, player2)
    game.run()


if __name__ == "__main__":
    main()
