from __future__ import print_function

from display import Display
from piece import Piece


class Manager:
    MOVES = {
        'a': 'move_left',
        'd': 'move_right',
        'w': 'rotate_counter_clockwise',
        's': 'rotate_clockwise'
    }

    def __init__(self):
        self.display = Display()
        self._spawn_piece()

    def _spawn_piece(self):
        self.current_piece = Piece()
        self.display.add_piece(self.current_piece)
        self.display.draw()

    def game_loop(self):
        user_input = raw_input('Please enter a move: ').strip()
        move = self.MOVES.get(user_input)

        if move is None:
            print('Entered move does not exist! Try again.')
            return self.game_loop()

        bound = self.display.get_piece_bound()
        move = getattr(self.current_piece, move)

        if not move(bound):
            print('Invalid move! Try again.')
            return self.game_loop()

        self.current_piece.y += 1

