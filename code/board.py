from code.exceptions import InvalidMove


class Coord:
    column: int
    row: int

    def __init__(self, column, row):
        self.column = column
        self.row = row
        self._validate()

    def _validate(self):
        INVALID_VALUE_FOR_COORD_MSG = "Invalid value for {}, should be one of [0, 1, 2]"
        if self.column not in [0, 1, 2]:
            raise InvalidMove(INVALID_VALUE_FOR_COORD_MSG.format("column"))
        elif self.row not in [0, 1, 2]:
            raise InvalidMove(INVALID_VALUE_FOR_COORD_MSG.format("row"))


class Board:
    def __init__(self):
        self._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def make_a_move(self, coord: Coord, player_value: int):
        self._validate_move(coord)
        self._data[coord.row][coord.column] = player_value

    def _validate_move(self, coord: Coord):
        pass