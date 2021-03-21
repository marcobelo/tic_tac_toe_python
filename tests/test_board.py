from code.board import Board, Coord
from code.exceptions import InvalidCoord

import pytest


def test_create_new_board():
    expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    board = Board()
    assert board._data == expected_result


def test_make_a_move():
    expected_result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    board = Board()
    board.make_a_move(Coord(1, 1), 1)

    assert board._data == expected_result


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
