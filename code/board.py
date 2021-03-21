class Board(list):
    def __init__(self):
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super(Board, self).__init__(board)

    def make_a_move(self, x, y, player_value):
        self[y][x] = player_value
