from __future__ import annotations

from typing import List, Optional

from ..models.chess_set_manager import ChessSetManager

from ..models.board import Board


class WebView:
    """Renders the chess board as HTML for the web interface."""

    def __init__(self, chess_set_manager: ChessSetManager) -> None:
        self.chess_set_manager = chess_set_manager

    def render(
        self,
        board: Board,
        current_player: str,
        set_name: str,
        available_sets: List[str],
        message: str = "",
        move_history: Optional[List[str]] = None,
    ) -> str:
        board_state = board.board_state_for_display()
        history = move_history or []
        html_lines: List[str] = []
        html_lines.append("<html><head><meta charset='utf-8'>")
        html_lines.append("<style>")
        html_lines.append("table{border-collapse:collapse;}")
        html_lines.append(
            "td{width:40px;height:40px;text-align:center;font-size:24px;}"
        )
        html_lines.append(".light{background:#eee;}")
        html_lines.append(".dark{background:#666;color:white;}")
        html_lines.append(".selected{outline:2px solid red;}")
        html_lines.append(".container{display:flex;}")
        html_lines.append(".history{margin-left:20px;}")
        html_lines.append("img{width:40px;height:40px;}")
        html_lines.append("</style></head><body>")
        if message:
            html_lines.append(f"<p>{message}</p>")
        html_lines.append(f"<p>Current player: {current_player}</p>")
        html_lines.append("<form method='POST' action='/set'>")
        html_lines.append("<label for='set'>Chess Set:</label>")
        html_lines.append("<select id='set' name='set' onchange='this.form.submit()'>")
        for name in available_sets:
            selected_attr = " selected" if name == set_name else ""
            html_lines.append(f"<option value='{name}'{selected_attr}>{name}</option>")
        html_lines.append("</select></form>")
        html_lines.append("<div class='container'>")
        html_lines.append("<div id='board'>")
        html_lines.append("<table>")
        for row in range(7, -1, -1):
            html_lines.append("<tr>")
            for column in range(8):
                piece = board_state[row][column]
                cell_class = "light" if (row + column) % 2 == 0 else "dark"
                if piece == ".":
                    cell_content = "&nbsp;"
                else:
                    img_path = self.chess_set_manager.image_path_for(set_name, piece)
                    cell_content = f"<img src='/static/{img_path}' alt='{piece}'>"
                position = Board.coords_to_position((row, column))
                html_lines.append(
                    f"<td class='{cell_class}' data-pos='{position}'>{cell_content}</td>"
                )
            html_lines.append("</tr>")
        html_lines.append("</table>")
        html_lines.append("</div>")
        html_lines.append("<div class='history'>")
        html_lines.append("<h3>Move History</h3><ol>")
        for move in history:
            html_lines.append(f"<li>{move}</li>")
        html_lines.append("</ol></div></div>")
        html_lines.append(
            "<script>const cells=document.querySelectorAll('#board td');let selected=null;cells.forEach(c=>c.addEventListener('click',()=>{const pos=c.dataset.pos;if(!selected){selected=pos;c.classList.add('selected');}else{fetch('/move',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({start:selected,end:pos})}).then(()=>location.reload());}}));</script>"
        )
        html_lines.append("</body></html>")
        return "\n".join(html_lines)
