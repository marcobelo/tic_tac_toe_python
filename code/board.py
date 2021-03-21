from code.exceptions import InvalidMove


class Board:
    def __init__(self):
        self._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def make_a_move(self, x, y, player_value):
        self._validate_move(x, y)
        self._data[y][x] = player_value

    def _validate_move(self, x, y):
        INVALID_VALUE_FOR_COORD_MSG = "Invalid value for {}, should be one of [0, 1, 2]"
        if x not in [0, 1, 2]:
            raise InvalidMove(INVALID_VALUE_FOR_COORD_MSG.format("column"))
        elif y not in [0, 1, 2]:
            raise InvalidMove(INVALID_VALUE_FOR_COORD_MSG.format("row"))