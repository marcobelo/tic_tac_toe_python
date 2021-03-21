from code.board import Board
from code.coord import Coord
from code.exceptions import InvalidMove

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


def test_set_and_get_value():
    expected_value = 3
    board = Board()
    board._set_value(Coord(1, 2), expected_value)
    result_value = board._get_value(Coord(1, 2))
    assert result_value == expected_value


def test_move_to_an_occupied_coord_raise_InvalidMove_exception():
    board = Board()
    board.make_a_move(Coord(1, 1), 1)
    with pytest.raises(InvalidMove) as exception:
        board.make_a_move(Coord(1, 1), 1)
    assert exception.value.message == "Invalid move, this position is already occupied"
