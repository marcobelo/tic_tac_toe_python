from code.board import Board


def test_create_new_board():
    expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    board = Board()
    assert board == expected_result


def test_make_a_move():
    expected_result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    player_value = 1
    board = Board()
    board.make_a_move(1, 1, player_value)

    assert board == expected_result
