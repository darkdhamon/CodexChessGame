from __future__ import annotations

from typing import List

from ..models.board import Board


class WebView:
    """Renders the chess board as HTML for the web interface."""

    def render(self, board: Board, current_player: str, message: str = "") -> str:
        board_state = board.board_state_for_display()
        html_lines: List[str] = []
        html_lines.append("<html><head><meta charset='utf-8'>")
        html_lines.append("<style>")
        html_lines.append("table{border-collapse:collapse;}")
        html_lines.append(
            "td{width:40px;height:40px;text-align:center;font-size:24px;}"
        )
        html_lines.append(".light{background:#eee;}")
        html_lines.append(".dark{background:#666;color:white;}")
        html_lines.append("</style></head><body>")
        if message:
            html_lines.append(f"<p>{message}</p>")
        html_lines.append(f"<p>Current player: {current_player}</p>")
        html_lines.append(
            "<form action='/move' method='post'>"
            "<input type='text' name='move' placeholder='e2 e4' autofocus> "
            "<input type='submit' value='Move'>"
            "</form>"
        )
        html_lines.append("<table>")
        for row in range(7, -1, -1):
            html_lines.append("<tr>")
            for column in range(8):
                piece = board_state[row][column]
                cell_class = "light" if (row + column) % 2 == 0 else "dark"
                cell_content = "&nbsp;" if piece == "." else piece
                html_lines.append(f"<td class='{cell_class}'>{cell_content}</td>")
            html_lines.append("</tr>")
        html_lines.append("</table></body></html>")
        return "\n".join(html_lines)
