from code.coord import Coord


class Board:
    def __init__(self):
        self._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def make_a_move(self, coord: Coord, player_value: int):
        self._validate_move(coord)
        self._data[coord.row][coord.column] = player_value

    def _validate_move(self, coord: Coord):
        pass