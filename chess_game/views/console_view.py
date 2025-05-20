from __future__ import annotations

import os
from ..models.board import Board


class ConsoleView:
    """Handles command-line interaction with the user."""

    WHITE_BACKGROUND = "\033[47m"
    BLACK_BACKGROUND = "\033[40m"
    WHITE_PIECE_FOREGROUND = "\033[34m"  # blue
    BLACK_PIECE_FOREGROUND = "\033[31m"  # red
    RESET = "\033[0m"

    def __init__(self) -> None:
        if os.name == "nt":
            self._enable_windows_ansi_support()

    def _enable_windows_ansi_support(self) -> None:
        """Enable ANSI escape code interpretation on Windows consoles."""
        try:
            import ctypes

            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_uint32()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception:
            # Fallback silently when unable to modify console mode
            pass

    def _colored_square(self, piece_symbol: str, row: int, column: int) -> str:
        """Return a board square formatted with colors."""
        is_light_square = (row + column) % 2 == 0
        background = (
            self.WHITE_BACKGROUND if is_light_square else self.BLACK_BACKGROUND
        )

        if piece_symbol == ".":
            return f"{background} {self.RESET}"

        foreground = (
            self.WHITE_PIECE_FOREGROUND
            if piece_symbol.isupper()
            else self.BLACK_PIECE_FOREGROUND
        )
        return f"{background}{foreground}{piece_symbol}{self.RESET}"

    def display_board(self, board: Board) -> None:
        state = board.board_state_for_display()
        print("  a b c d e f g h")
        for row in range(7, -1, -1):
            colored_line = [
                self._colored_square(state[row][col], row, col) for col in range(8)
            ]
            print(str(row + 1) + " " + " ".join(colored_line) + self.RESET)
        print()

    def prompt_move(self, player: str) -> str:
        return input(f"{player} move (e.g., e2 e4) or 'quit': ")

    def invalid_input(self) -> None:
        print("Invalid input. Enter moves like 'e2 e4'.")

    def invalid_move(self) -> None:
        print("Invalid move. Try again.")
