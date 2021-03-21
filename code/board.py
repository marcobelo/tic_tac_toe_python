class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def make_a_move(self, x, y, player_value):
        self.board[y][x] = player_value