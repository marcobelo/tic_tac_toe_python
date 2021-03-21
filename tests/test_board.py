from code.board import Board
from code.coord import Coord


def test_create_new_board():
    expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    board = Board()
    assert board._data == expected_result


def test_make_a_move():
    expected_result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    board = Board()
    board.make_a_move(Coord(1, 1), 1)

    assert board._data == expected_result
