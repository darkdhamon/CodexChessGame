from __future__ import annotations

from ..models.board import Board


class ConsoleView:
    """Handles command-line interaction with the user."""

    def display_board(self, board: Board) -> None:
        state = board.board_state_for_display()
        print("  a b c d e f g h")
        for row in range(7, -1, -1):
            line = [state[row][col] for col in range(8)]
            print(str(row + 1) + " " + " ".join(line))
        print()

    def prompt_move(self, player: str) -> str:
        return input(f"{player} move (e.g., e2 e4) or 'quit': ")

    def invalid_input(self) -> None:
        print("Invalid input. Enter moves like 'e2 e4'.")

    def invalid_move(self) -> None:
        print("Invalid move. Try again.")
