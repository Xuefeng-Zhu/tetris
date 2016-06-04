from __future__ import print_function
import copy

from config import HEIGHT, WIDTH, ACTIONS, OverlapError


class Display:
    def __init__(self):
        self.current_piece = None
        self.board = [[False] * WIDTH for _ in range(HEIGHT)]

    def draw(self):
        '''
            Print out tetris board
        '''
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
        '''
            Add a new piece into the board
        '''
        self.current_piece = piece
        self.old_board = copy.deepcopy(self.board)
        self.show_piece(True)

    def show_piece(self, new_piece=False):
        '''
            update the board values to show current piece position
        '''
        cp = self.current_piece

        if not new_piece:
            self.board = copy.deepcopy(self.old_board)

        for i, row in enumerate(cp.shape):
            for j, elm in enumerate(row):
                if elm:
                    y = cp.y - (cp.bottom - i)
                    x = cp.x + (j - cp.left)

                    if x < 0 or x >= WIDTH or \
                            y < 0 or y >= HEIGHT:
                        raise OverlapError

                    if self.board[y][x]:
                        raise OverlapError

                    self.board[y][x] = True

    def check_valid_moves(self):
        '''
            Check if there is possible valid movements for current piece
        '''
        if self.current_piece.y == HEIGHT - 1:
            return False

        cp = self.current_piece

        for action in ACTIONS.values():
            self.current_piece = copy.deepcopy(cp)
            self.current_piece.move(action)

            try:
                self.show_piece()
                self.current_piece = cp
                self.show_piece()
                return True
            except OverlapError:
                pass

        self.current_piece = cp
        self.show_piece()
        return False

    def update_board(self):
        '''
            Update board to eliminate row has been fully filled
        '''
        if not self.current_piece:
            return

        cp = self.current_piece
        for row in self.board[cp.y:cp.y - cp.height:-1]:
            if all(row):
                self.board.remove(row)
                self.board.insert(0, [False] * WIDTH)
