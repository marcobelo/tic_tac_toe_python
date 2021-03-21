from code.coord import Coord
from code.exceptions import InvalidMove

AVAILABLE_COORD = 0


class Board:
    def __init__(self):
        self._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def make_a_move(self, coord: Coord, player_value: int):
        self._validate_move(coord)
        self._set_value(coord, player_value)

    def _validate_move(self, coord: Coord):
        if self._get_value(coord) != AVAILABLE_COORD:
            raise InvalidMove("Invalid move, this position is already occupied")

    def _set_value(self, coord: Coord, value):
        self._data[coord.row][coord.column] = value

    def _get_value(self, coord: Coord):
        return self._data[coord.row][coord.column]