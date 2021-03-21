from code.coord import Coord
from code.exceptions import InvalidCoord

import pytest


@pytest.mark.parametrize("column", [-1, 3])
def test_invalid_coord_column_value_should_raise_InvalidCoord_exception(column):
    with pytest.raises(InvalidCoord) as exception:
        Coord(column, 1)
    assert (
        exception.value.message
        == "Invalid value for column, should be one of [0, 1, 2]"
    )


@pytest.mark.parametrize("row", [-1, 3])
def test_invalid_coord_row_value_should_raise_InvalidCoord_exception(row):
    with pytest.raises(InvalidCoord) as exception:
        Coord(1, row)
    assert (
        exception.value.message == "Invalid value for row, should be one of [0, 1, 2]"
    )


@pytest.mark.parametrize("column, row", [(-1, -1), (3, 3)])
def test_invalid_coord_row_value_should_raise_InvalidCoord_exception22(column, row):
    with pytest.raises(InvalidCoord) as exception:
        Coord(column, row)
    assert (
        exception.value.message
        == "Invalid value for column and row, should be one of [0, 1, 2]"
    )
