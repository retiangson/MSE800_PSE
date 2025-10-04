# Tic-Tac-Toe (Noughts and Crosses)

**Programming Paradigm:** Object-Oriented
**Design Approach:** Top-Down & Functionally Decomposed
**Focus:** Readability • Maintainability • Pylint compliance

---

## Project Overview

A simple 3×3 Tic-Tac-Toe game written in Python 3 demonstrating clean OOP design, top-down decomposition, and adherence to PEP-8/Pylint style guidelines.

Players alternate turns, entering their chosen cell using a **two-digit coordinate** (e.g. `11`, `12`, `23`).
The program validates input, detects wins/draws, and displays results clearly on the console.

---

## 📁 Project Structure

```
tic_tac_toe/
│
├── main.py         → Entry point; initializes and runs the game
├── game.py         → Controls game flow and rules
├── board.py        → Represents and manages the grid
├── player.py       → Handles player logic and input
└── utils.py        → Optional helpers and constants
```

---

## Class and Method Design (Top-Down)

### Class `Board`

| Method                          | Description                   |
| :------------------------------ | :---------------------------- |
| `__init__(size: int = 3)`       | Initialize empty board        |
| `display()`                     | Print board state             |
| `update_cell(row, col, symbol)` | Place mark if cell is empty   |
| `is_full()`                     | Check if board is full        |
| `check_winner()`                | Determine if there’s a winner |
| `reset()`                       | Clear the board for replay    |

---

### 🎮 Class `Player`

| Method                   | Description                                    |
| :----------------------- | :--------------------------------------------- |
| `__init__(name, symbol)` | Initialize player                              |
| `make_move(board)`       | Prompt for move (two-digit input) and validate |
| `is_human()`             | Placeholder for possible AI extension          |

> 💡 Input format: enter two digits without spaces or commas — e.g. `11` (row 1 col 1), `23` (row 2 col 3).

---

### Class `Game`

| Method                       | Description                               |
| :--------------------------- | :---------------------------------------- |
| `__init__(player1, player2)` | Initialize game and show coordinate guide |
| `display_reference_board()`  | Show coordinate map (11–33) at start      |
| `switch_player()`            | Alternate between players                 |
| `play_turn()`                | Execute one player’s turn                 |
| `is_game_over()`             | Check for win or draw                     |
| `get_winner()`               | Return winning player                     |
| `run()`                      | Main game loop                            |

---

### Module `utils.py`

Optional helper utilities and constants such as:

```python
BOARD_SIZE = 3
EMPTY_CELL = " "
```

---

## Coordinate Guide (Displayed Automatically)

When the game starts, a reference board helps players understand valid move codes:

```
📍 Coordinate Guide:
 11 | 12 | 13
---+---+---
 21 | 22 | 23
---+---+---
 31 | 32 | 33
```

---

## How to Play

1. Run the program:

   ```bash
   python main.py
   ```
2. Enter player names.
3. Each turn, type a **two-digit number** to choose your cell.

   * Example: `22` means row 2 column 2
4. The program displays the board after each move and announces the winner or draw.

---

## Testing Summary

| Test           | Input             | Expected Result              |
| :------------- | :---------------- | :--------------------------- |
| Valid move     | `11`              | Mark placed in row 1 col 1   |
| Occupied cell  | Repeat `11`       | “Cell already taken” message |
| Invalid format | `a1` / `123`      | “Invalid format” message     |
| Out-of-range   | `44`              | “Invalid range” message      |
| Full row win   | X: `11 12 13`     | “X wins!”                 |
| Diagonal win   | O: `11 22 33`     | “O wins!”                 |
| Full board     | Alternating moves | “It’s a draw!”            |

---
