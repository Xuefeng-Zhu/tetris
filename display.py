from __future__ import print_function
import copy

from config import HEIGHT, WIDTH, OverlapError


class Display:
    def __init__(self):
        self.board = [[False] * WIDTH for _ in range(HEIGHT)]

    def draw(self):
        for row in self.board:
            print('*', end='')
            for elm in row:
                if elm:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('*')

        print('*' * (WIDTH + 2))

    def add_piece(self, piece):
        self.current_piece = piece
        self.old_board = copy.deepcopy(self.board)
        self.show_piece(True)

    def show_piece(self, new_piece=False):
        cp = self.current_piece

        if not new_piece:
            self.board = copy.deepcopy(self.board)

        for i, row in enumerate(cp.shape):
            for j, elm in enumerate(row):
                if elm:
                    x = cp.x + (i - cp.left)
                    y = cp.y - (cp.bottom - j)
                    self.board[y][x] = True

    def get_piece_bound(self):
        cp = self.current_piece
        bound = {
            'left': 0,
            'right': WIDTH - 1
        }
        row = self.board(cp.y)

        for i in range(cp.x - 1, 0, -1):
            if row[i]:
                bound['left'] = i
                break

        for i in range(cp.x + 1, WIDTH):
            if row[i]:
                bound['right'] = i
                break

    def check_valid_moves(self):
        if self.current_piece.y == HEIGHT - 1:
            return False

        cp = self.current_piece
        self.current_piece = copy.deepcopy(cp)
        self.current_piece.y += 1

        bound = self.get_piece_bound()
