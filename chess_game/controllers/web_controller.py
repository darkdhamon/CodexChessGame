from __future__ import annotations

from typing import List, Optional

from flask import Flask, request

from ..models.board import Board
from ..views.web_view import WebView


class WebController:
    """Flask-based controller to play chess in a browser."""

    def __init__(self) -> None:
        self.board = Board()
        self.current_player = "white"
        self.move_history: List[str] = []
        self.view = WebView()
        self.app = Flask(__name__)
        self._register_routes()

    def _register_routes(self) -> None:
        @self.app.route("/", methods=["GET"])
        def index() -> str:
            return self.view.render(
                self.board, self.current_player, move_history=self.move_history
            )

        @self.app.route("/move", methods=["POST"])
        def move() -> str:
            data = request.get_json(silent=True)
            if data:
                start_text = data.get("start", "")
                end_text = data.get("end", "")
                move_text = f"{start_text} {end_text}"
            else:
                move_text = request.form.get("move", "")

            feedback = ""
            parsed_move = self._parse_move(move_text)
            if parsed_move is None:
                feedback = "Invalid input. Use format 'e2 e4'."
            else:
                start, end = parsed_move
                piece = self.board.get_piece(start)
                if (
                    piece is None
                    or piece.color != self.current_player
                    or end not in piece.valid_moves(start, self.board)
                ):
                    feedback = "Invalid move."
                else:
                    self.board.move_piece(start, end)
                    self.move_history.append(
                        f"{Board.coords_to_position(start)}-{Board.coords_to_position(end)}"
                    )
                    self.current_player = (
                        "black" if self.current_player == "white" else "white"
                    )
            return self.view.render(
                self.board,
                self.current_player,
                feedback,
                move_history=self.move_history,
            )

    def _parse_move(self, user_input: str) -> Optional[tuple[tuple[int, int], tuple[int, int]]]:
        parts = user_input.strip().split()
        if len(parts) != 2:
            return None
        try:
            start = Board.position_to_coords(parts[0])
            end = Board.position_to_coords(parts[1])
            return start, end
        except Exception:
            return None

    def run(self, **kwargs: object) -> None:
        self.app.run(**kwargs)
