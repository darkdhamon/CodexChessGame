"""Manage available chess sets and provide paths to piece images."""

from __future__ import annotations

import os
from pathlib import Path
from typing import List


class ChessSetManager:
    """Handles discovery of chess sets and image path generation."""

    def __init__(self, assets_path: Path) -> None:
        self.assets_path = assets_path
        self.chess_sets_path = self.assets_path / "ChessSets"
        self.available_sets = self._discover_sets()

    def _discover_sets(self) -> List[str]:
        if not self.chess_sets_path.exists():
            return []
        return [d.name for d in self.chess_sets_path.iterdir() if d.is_dir()]

    def image_path_for(self, set_name: str, symbol: str) -> str:
        """Return relative path to the piece image."""
        piece_names = {
            "k": "King",
            "q": "Queen",
            "r": "Rook",
            "b": "Bishop",
            "n": "Knight",
            "p": "Pawn",
        }
        color_prefix = "W" if symbol.isupper() else "B"
        piece_name = piece_names.get(symbol.lower(), "")
        file_name = f"{color_prefix}_{piece_name}.png"
        return os.path.join("ChessSets", set_name, file_name)

