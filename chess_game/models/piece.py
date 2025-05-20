from abc import ABC, abstractmethod


class Piece(ABC):
    """Base class for all chess pieces."""

    def __init__(self, color: str):
        self.color = color

    @property
    @abstractmethod
    def symbol(self) -> str:
        """Return the single-character symbol for the piece."""

    @abstractmethod
    def valid_moves(self, position: tuple[int, int], board: 'Board') -> list[tuple[int, int]]:
        """Return a list of valid target squares for this piece."""


class King(Piece):
    @property
    def symbol(self) -> str:
        return 'K' if self.color == 'white' else 'k'

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        for r_delta in (-1, 0, 1):
            for c_delta in (-1, 0, 1):
                if r_delta == 0 and c_delta == 0:
                    continue
                target = (row + r_delta, col + c_delta)
                if board.is_within_bounds(target) and board.is_open_for(target, self.color):
                    moves.append(target)
        return moves


class Queen(Piece):
    @property
    def symbol(self) -> str:
        return 'Q' if self.color == 'white' else 'q'

    def valid_moves(self, position, board):
        return Rook(self.color).valid_moves(position, board) + \
               Bishop(self.color).valid_moves(position, board)


class Rook(Piece):
    @property
    def symbol(self) -> str:
        return 'R' if self.color == 'white' else 'r'

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r_delta, c_delta in directions:
            r, c = row + r_delta, col + c_delta
            while board.is_within_bounds((r, c)):
                if board.is_empty((r, c)):
                    moves.append((r, c))
                else:
                    if board.get_piece((r, c)).color != self.color:
                        moves.append((r, c))
                    break
                r += r_delta
                c += c_delta
        return moves


class Bishop(Piece):
    @property
    def symbol(self) -> str:
        return 'B' if self.color == 'white' else 'b'

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for r_delta, c_delta in directions:
            r, c = row + r_delta, col + c_delta
            while board.is_within_bounds((r, c)):
                if board.is_empty((r, c)):
                    moves.append((r, c))
                else:
                    if board.get_piece((r, c)).color != self.color:
                        moves.append((r, c))
                    break
                r += r_delta
                c += c_delta
        return moves


class Knight(Piece):
    @property
    def symbol(self) -> str:
        return 'N' if self.color == 'white' else 'n'

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        candidates = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        for target in candidates:
            if board.is_within_bounds(target) and board.is_open_for(target, self.color):
                moves.append(target)
        return moves


class Pawn(Piece):
    @property
    def symbol(self) -> str:
        return 'P' if self.color == 'white' else 'p'

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        direction = 1 if self.color == 'white' else -1
        start_row = 1 if self.color == 'white' else 6
        forward = (row + direction, col)
        if board.is_within_bounds(forward) and board.is_empty(forward):
            moves.append(forward)
            two_forward = (row + 2 * direction, col)
            if row == start_row and board.is_empty(two_forward):
                moves.append(two_forward)
        for c_delta in (-1, 1):
            capture = (row + direction, col + c_delta)
            if board.is_within_bounds(capture) and not board.is_empty(capture):
                if board.get_piece(capture).color != self.color:
                    moves.append(capture)
        return moves
