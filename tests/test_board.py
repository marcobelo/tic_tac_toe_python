from code.board import Board
from code.exceptions import InvalidMove

import pytest


def test_create_new_board():
    expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    board = Board()
    assert board._data == expected_result


def test_make_a_move():
    expected_result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    board = Board()
    board.make_a_move(1, 1, 1)

    assert board._data == expected_result


@pytest.mark.parametrize("column", [-1, 3])
def test_invalid_column_value_should_raise_InvalidMove_exception(column):
    board = Board()
    with pytest.raises(InvalidMove) as exception:
        board.make_a_move(column, 1, 1)

    assert (
        exception.value.message
        == "Invalid value for column, should be one of [0, 1, 2]"
    )


@pytest.mark.parametrize("row", [-1, 3])
def test_invalid_row_value_should_raise_InvalidMove_exception(row):
    board = Board()
    with pytest.raises(InvalidMove) as exception:
        board.make_a_move(1, row, 1)

    assert (
        exception.value.message == "Invalid value for row, should be one of [0, 1, 2]"
    )
