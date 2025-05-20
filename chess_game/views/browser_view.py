from __future__ import annotations

import os
import webbrowser
from typing import List

from ..models.board import Board
from .base_view import BaseView


class BrowserView(BaseView):
    """Displays the chess board in a web browser."""

    def __init__(self, html_file: str = "board.html") -> None:
        self.html_file = html_file
        self.browser_opened = False

    def display_board(self, board: Board) -> None:
        html_content = self._generate_html(board)
        with open(self.html_file, "w", encoding="utf-8") as file_handle:
            file_handle.write(html_content)
        if not self.browser_opened:
            webbrowser.open(f"file://{os.path.abspath(self.html_file)}")
            self.browser_opened = True

    def prompt_move(self, player: str) -> str:
        return input(f"{player} move (e.g., e2 e4) or 'quit': ")

    def invalid_input(self) -> None:
        print("Invalid input. Enter moves like 'e2 e4'.")

    def invalid_move(self) -> None:
        print("Invalid move. Try again.")

    def _generate_html(self, board: Board) -> str:
        state = board.board_state_for_display()
        html_lines: List[str] = []
        html_lines.append("<html><head><meta charset='utf-8'>")
        html_lines.append("<style>")
        html_lines.append("table { border-collapse: collapse; }")
        html_lines.append(
            "td { width: 40px; height: 40px; text-align: center; font-size: 24px; }"
        )
        html_lines.append(".light { background: #eee; }")
        html_lines.append(".dark { background: #666; color: white; }")
        html_lines.append("</style></head><body>")
        html_lines.append("<table>")
        for row in range(7, -1, -1):
            html_lines.append("<tr>")
            for col in range(8):
                piece = state[row][col]
                cell_class = "light" if (row + col) % 2 == 0 else "dark"
                cell_content = "&nbsp;" if piece == "." else piece
                html_lines.append(f"<td class='{cell_class}'>{cell_content}</td>")
            html_lines.append("</tr>")
        html_lines.append("</table></body></html>")
        return "\n".join(html_lines)
