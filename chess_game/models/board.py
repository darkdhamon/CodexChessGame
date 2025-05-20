from __future__ import annotations

from typing import Optional

from .piece import (
    Piece,
    Pawn,
    Rook,
    Knight,
    Bishop,
    Queen,
    King,
)


class Board:
    """Represents the state of the chess board."""

    def __init__(self) -> None:
        self.grid: list[list[Optional[Piece]]] = [[None for _ in range(8)] for _ in range(8)]
        self._setup_starting_position()

    @staticmethod
    def position_to_coords(pos: str) -> tuple[int, int]:
        """Convert algebraic position like 'e2' to (row, col)."""
        col = ord(pos[0].lower()) - ord('a')
        row = int(pos[1]) - 1
        return row, col

    @staticmethod
    def coords_to_position(coords: tuple[int, int]) -> str:
        row, col = coords
        return chr(col + ord('a')) + str(row + 1)

    def _setup_starting_position(self) -> None:
        """Place all pieces on the board in the initial configuration."""
        for col in range(8):
            self.grid[1][col] = Pawn('white')
            self.grid[6][col] = Pawn('black')
        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(placement):
            self.grid[0][col] = piece_class('white')
            self.grid[7][col] = piece_class('black')

    def get_piece(self, coords: tuple[int, int]) -> Optional[Piece]:
        row, col = coords
        return self.grid[row][col]

    def set_piece(self, coords: tuple[int, int], piece: Optional[Piece]) -> None:
        row, col = coords
        self.grid[row][col] = piece

    def is_within_bounds(self, coords: tuple[int, int]) -> bool:
        row, col = coords
        return 0 <= row < 8 and 0 <= col < 8

    def is_empty(self, coords: tuple[int, int]) -> bool:
        return self.get_piece(coords) is None

    def is_open_for(self, coords: tuple[int, int], color: str) -> bool:
        target = self.get_piece(coords)
        return target is None or target.color != color

    def move_piece(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        piece = self.get_piece(start)
        self.set_piece(end, piece)
        self.set_piece(start, None)

    def board_state_for_display(self) -> list[list[str]]:
        display = [['.' for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece:
                    display[row][col] = piece.symbol
        return display
