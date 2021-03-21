from code.board import Board


def test_create_new_board():
    board = Board()
    assert board.board == [[0,0,0], [0,0,0], [0,0,0]]