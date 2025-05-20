from __future__ import annotations

from typing import Optional

from ..models.board import Board
from ..models.piece import Piece
from ..views.console_view import ConsoleView


class GameController:
    """Coordinates the interactions between view and model."""

    def __init__(self, view: ConsoleView) -> None:
        self.board = Board()
        self.view = view
        self.current_player = 'white'

    def parse_move(self, user_input: str) -> Optional[tuple[tuple[int, int], tuple[int, int]]]:
        parts = user_input.strip().split()
        if len(parts) != 2:
            return None
        try:
            start = Board.position_to_coords(parts[0])
            end = Board.position_to_coords(parts[1])
            return start, end
        except Exception:
            return None

    def run(self) -> None:
        while True:
            self.view.display_board(self.board)
            user_input = self.view.prompt_move(self.current_player)
            if user_input.lower() in {"quit", "exit"}:
                print("Exiting game.")
                break
            parsed = self.parse_move(user_input)
            if not parsed:
                self.view.invalid_input()
                continue
            start, end = parsed
            piece = self.board.get_piece(start)
            if piece is None or piece.color != self.current_player:
                self.view.invalid_move()
                continue
            if end not in piece.valid_moves(start, self.board):
                self.view.invalid_move()
                continue
            self.board.move_piece(start, end)
            self.current_player = 'black' if self.current_player == 'white' else 'white'
