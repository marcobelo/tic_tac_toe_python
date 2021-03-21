from code.exceptions import InvalidCoord


class Coord:
    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row
        self._validate()

    def _validate(self):
        invalid_coords = []
        if self.column not in [0, 1, 2]:
            invalid_coords.append("column")
        if self.row not in [0, 1, 2]:
            invalid_coords.append("row")
        if invalid_coords:
            raise InvalidCoord(
                f"Invalid value for {' and '.join(invalid_coords)}, should be one of [0, 1, 2]"
            )
