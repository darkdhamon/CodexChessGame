from __future__ import annotations

from abc import ABC, abstractmethod

from ..models.board import Board


class BaseView(ABC):
    """Abstract base class for all user interface views."""

    @abstractmethod
    def display_board(self, board: Board) -> None:
        """Show the board state to the user."""
        raise NotImplementedError

    @abstractmethod
    def prompt_move(self, player: str) -> str:
        """Ask the player for their move and return the raw input."""
        raise NotImplementedError

    @abstractmethod
    def invalid_input(self) -> None:
        """Notify the user about invalid input."""
        raise NotImplementedError

    @abstractmethod
    def invalid_move(self) -> None:
        """Notify the user about an invalid move."""
        raise NotImplementedError
